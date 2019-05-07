#!/usr/bin/env python


import requests

baseurl="https://api.niwa.co.nz/uv/data"
towns=[["Auckland", 174, -42], ["Hamilton", 174, -41], ["Wellington", 174, -40] ]
apikey=""
product=1 # 1 = cloudy sky, 0 = clear sky



def get(url, params=None):
  if not params:
    params = {}
  headers = {'Content-Type' : 'application/json'}
  return requests.get(url, params=params, headers=headers)


#import urllib.request, json 
#with urllib.request.urlopen("https://api-dev.niwa.co.nz/uv/data?${coords[$i]}&apikey=$apikey") as url:
#    data = json.loads(url.read().decode())
#    print(data)

with open("/out/uvi-nzmet.csv","w+") as f:
  for i in range(len(towns)):
    print(towns[i])
    print(i)
    response = get(baseurl, params={'apikey': apikey, 'lat':towns[i][2], 'long':towns[i][1]})
    uvjson = response.json()
    values = uvjson['products'][product]['values']
    print(values)
    f.write(towns[i][0] +"\r\n")
    for j in range(len(values)):
      print(values[j]['time'])
      f.write(values[j]['time']+",")

    f.write("\r\n")
    for k in range(len(values)):
      print(values[k]['value'])
      f.write(str(values[i]['value'])+",")
    f.write("\r\n")
    f.write("\r\n")
