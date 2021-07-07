import pandas as pd
from datetime import datetime, timedelta


def convert_to_datetime(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y %H:%M")


trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')

start_times = list(map(convert_to_datetime, trips['start_at'].tolist()))
end_times = list(map(convert_to_datetime, trips['end_at'].tolist()))

start_times.sort()
end_times.sort(reverse=True)

print(start_times[0])
print(end_times[0])
