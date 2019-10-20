import requests
import time
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

for i in range(len(trips_id)):
    start_req = requests.get(url.format(starts_lat[i], starts_lon[i]))
    print((trips_id[i], start_req.json()))
    time.sleep(5)

for i in range(len(trips_id)):
    end_req = requests.get(url.format(ends_lat[i], ends_lon[i]))
    print((trips_id[i], end_req.json()))
    time.sleep(5)

print(starts_ubigeo)
print("-----------")
print(ends_ubigeo)
