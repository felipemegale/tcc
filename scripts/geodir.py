import time
import json
import requests
import pandas as pd

url = "https://api.geodir.co/geocoder/geocoder-reverse/v1/findlatlon?y={0}&x={1}&token=b92005e0-814c-414e-8ac9-22c7d8c1ecf2"

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')
trips_id = trips['journey_id'].tolist()
starts_lat = trips['start_lat'].tolist()
starts_lon = trips['start_lon'].tolist()
starts_ubigeo = []
ends_lat = trips['end_lat'].tolist()
ends_lon = trips['end_lon'].tolist()
ends_ubigeo = []

with open("geodir_start.out", "w") as out:
    for i in range(len(trips_id)):
        start_req = requests.get(url.format(starts_lat[i], starts_lon[i]))
        out.write(trips_id[i]+"\n")
        out.write(json.dumps(start_req.json())+"\n")
        time.sleep(3)

with open("geodir_end.out", "w") as out:
    for i in range(len(trips_id)):
        end_req = requests.get(url.format(ends_lat[i], ends_lon[i]))
        out.write(trips_id[i]+"\n")
        out.write(json.dumps(end_req.json())+"\n")
        time.sleep(3)
