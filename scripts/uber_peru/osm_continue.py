import requests
import json
import pandas as pd
import json
import time

url = "https://us1.locationiq.com/v1/reverse.php"
api_key = 'ae15ec1cee4ce5'

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')
trips_id = trips['journey_id'].tolist()
starts_lat = trips['start_lat'].tolist()
starts_lon = trips['start_lon'].tolist()
starts_district = []
ends_lat = trips['end_lat'].tolist()
ends_lon = trips['end_lon'].tolist()
ends_district = []

with open("osm_end_continue.out", "w") as osm:
    for i in range(15930, len(trips_id)+1):
        data = {
            'key': api_key,
            'lat': ends_lat[i],
            'lon': ends_lon[i],
            'format': 'json'
        }
        req = requests.get(url, data)

        osm.write(req.text+"\n")
        time.sleep(8.5)
