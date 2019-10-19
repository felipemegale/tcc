import requests
import pandas as pd

url = "https://api.geodir.co/geocoder/geocoder-reverse/v1/findlatlon?y={0}&x={1}&token=b92005e0-814c-414e-8ac9-22c7d8c1ecf2"

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')
starts_lat = trips['start_lat'].tolist()
starts_lon = trips['start_lon'].tolist()
ends_lat = trips['end_lat'].tolist()
ends_lon = trips['end_lon'].tolist()

r = requests.get(url.format(starts_lat[0], starts_lon[0]))
print(r.json())
