import json
import requests
import wget 
import os
from os import path



# The links the the USGS earthquake data.
# Main URL https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
# URLs Used: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson

def main():
  url='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson'
  requrl=requests.get(url)
  geofile='1week_geo.json'


  print("URL Status code is: " + str(requrl.status_code))
  if requrl.status_code == 200:
    wget.download(url, geofile)
  else:
    print("Error occured while attempting to access URL, error code: " + str(requrl.status_code))

def printresults(data):
  print("Printing results function.")



if __name__ == '__main__':
  main()