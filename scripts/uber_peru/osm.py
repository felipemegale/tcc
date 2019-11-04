import requests
import json
import pandas as pd

url = "https://nominatim.openstreetmap.org/reverse.php?lat={0}&lon={1}&format=json"

trips = pd.read_csv("csv/uber_peru_ 2010_formatted_complete_fixed.csv", sep=';')
trips_id = trips['journey_id'].tolist()
starts_lat = trips['start_lat'].tolist()
starts_lon = trips['start_lon'].tolist()
starts_district = []
ends_lat = trips['end_lat'].tolist()
ends_lon = trips['end_lon'].tolist()
ends_district = []

