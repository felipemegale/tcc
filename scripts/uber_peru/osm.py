import requests
import json
import pandas as pd
import json
import time

url = "https://nominatim.openstreetmap.org/reverse.php?lat={0}&lon={1}&format=json"

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')
trips_id = trips['journey_id'].tolist()
starts_lat = trips['start_lat'].tolist()
starts_lon = trips['start_lon'].tolist()
starts_district = []
ends_lat = trips['end_lat'].tolist()
ends_lon = trips['end_lon'].tolist()
ends_district = []

with open("osm_start.out", "w") as osm:
    for i in range(len(trips_id)):
        req = requests.get(url.format(starts_lat[i], starts_lon[i]))
        osm.write(trips_id[i]+"\n")
        osm.write(json.dumps(req.json())+"\n")
        time.sleep(3)

with open("osm_end.out", "w") as osm:
    for i in range(len(trips_id)):
        req = requests.get(url.format(ends_lat[i], ends_lon[i]))
        osm.write(trips_id[i]+"\n")
        osm.write(json.dumps(req.json())+"\n")
        time.sleep(3)