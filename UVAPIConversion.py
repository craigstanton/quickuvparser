#!/usr/bin/env python

from os.path import join, dirname

import click
import logging
import requests


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
  with open(join(dirname(__file__), "out/uvi-nzmet.csv"), "w+") as f:
    for i, (town, long, lat) in enumerate(TOWNS):
      logging.debug(town)
      logging.debug(i)
      response = get(baseurl, params={'apikey': apikey, 'lat':lat, 'long':long})
      uvjson = response.json()
      values = uvjson['products'][product]['values']
      logging.debug(values)
      f.write(town + "\r\n")
      for j in range(len(values)):
        logging.debug(f"{values[j]['time']}")
        f.write(f"{values[j]['time']},")

      f.write("\r\n")
      for k in range(len(values)):
        logging.debug(f"{values[k]['value']}")
        f.write(f"{str(values[i]['value'])},")
      f.write("\r\n")
      f.write("\r\n")


if __name__ == "__main__":
  uvapi()
