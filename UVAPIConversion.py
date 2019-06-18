#!/usr/bin/env python

from os.path import join, dirname

import click
import logging
import requests
import csv
import datetime
import pytz

nz_tz = pytz.timezone('Pacific/Auckland')


logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)
TOWNS=[["Auckland", 174, -42], ["Hamilton", 174, -41], ["Wellington", 174, -40]]


def get(url, params=None):
  if not params:
    params = {}
  headers = {'Content-Type' : 'application/json'}
  return requests.get(url, params=params, headers=headers)


#import urllib.request, json 
#with urllib.request.urlopen("https://api-dev.niwa.co.nz/uv/data?${coords[$i]}&apikey=$apikey") as url:
#    data = json.loads(url.read().decode())
#    print(data)

@click.command()
@click.option("--baseurl", default="https://api.niwa.co.nz/uv/data", help="API base URL")
@click.option("--apikey", required=True, help="API key")
@click.option("--product", default=1, help="Product. 1 = cloudy sky, 0 = clear sky")
def uvapi(baseurl, apikey, product):
  first = True
  now = datetime.datetime.now()
  uvstart = now.astimezone(nz_tz).replace(hour=6,minute=0,second=0,microsecond=0)
  uvend = now.astimezone(nz_tz).replace(hour=19,minute=0,second=0,microsecond=0)
  
  
  with open(join(dirname(__file__), "/out/uvi-forecasts.csv"), "w+") as f:
  
    logging.debug("uvstart =" + uvstart.strftime("%Y-%m-%dT%H:%M:%S%z") + "\r\n")
    logging.debug("uvend =" + uvend.strftime("%Y-%m-%dT%H:%M:%S%z") + "\r\n")
    
    with open('sites.csv', newline='') as csvfile:
      sitereader = csv.DictReader(csvfile, delimiter=',', quotechar='\'')
      for site in sitereader:
        logging.debug(site['name'])
        response = get(baseurl, params={'apikey': apikey, 'lat':site['latitude'], 'long':site['longitude']})
        uvjson = response.json()
        values = uvjson['products'][product]['values']
        logging.debug(values)
        if (first) :
          for j in range(len(values)):
            d = datetime.datetime.strptime(values[j]['time'], "%Y-%m-%dT%H:%M:%S.000Z")
            #d.replace(tzinfo=UTC)
            nz = utc_to_nz(d)
            if ((nz >= uvstart) & (nz <= uvend)) :
              logging.debug(f"{values[j]['time']} = " + nz.strftime("%H:%M"))
              f.write(nz.strftime("%H:%M") + ",")
          first = False

        f.write("\r\n " + site['name'] + "\r\n ")
        
        for k in range(len(values)):
          utcTime = datetime.datetime.strptime(values[k]['time'], "%Y-%m-%dT%H:%M:%S.000Z")
          nzTime = utc_to_nz(utcTime)
          if ((nzTime >= uvstart) & (nzTime <= uvend)) :
            logging.debug(f"{values[k]['value']}")
            f.write("{:.2f}, ".format(values[k]['value']))


def utc_to_nz(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(nz_tz)
    return nz_tz.normalize(local_dt) # .normalize might be unnecessary
    

if __name__ == "__main__":
  uvapi()
