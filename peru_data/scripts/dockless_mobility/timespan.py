import pandas as pd
from datetime import datetime


def convert_string_to_date_time(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y %H:%M:%S %p")


print('reading file...')
trips = pd.read_csv('csv/dockless_2018.csv')
print('reading file... OK')

print('converting DF to list...')
starts = trips['Start Time'].tolist()
print('converting DF to list... OK')

print('mapping list...')
starts = list(map(convert_string_to_date_time, starts))
print('mapping list... OK')

print('sorting list...')
starts.sort()
print('sorting list... OK')
print(starts[0])

print('sorting list (reverse)...')
starts.sort(reverse=True)
print('sorting list (reverse)... OK')
print(starts[0])
