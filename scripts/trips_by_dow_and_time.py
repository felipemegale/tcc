import pandas as pd
from datetime import datetime


def get_day_of_week(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y %H:%M").strftime('%A')


trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')

starts = list(map(get_day_of_week, trips['start_at'].tolist()))

for start in range(0, 10):
    print(starts[start])
