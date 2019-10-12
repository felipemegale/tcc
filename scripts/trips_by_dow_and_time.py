import pandas as pd
import calcs


MORNING = 0
DAY = 1
NOON = 2
NIGHT = 3
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')
print(trips['journey_id'][0])
trips_list = trips['journey_id'].tolist()
starts = list(map(calcs.get_dow_and_time, trips['start_at'].tolist()))
groups = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []]
]

for trip in range(len(starts)):
    curr_start = starts[trip]
    if curr_start[0] == MONDAY:
        if calcs.is_morning(curr_start):
            groups[MONDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[MONDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[MONDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[MONDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == TUESDAY:
        if calcs.is_morning(curr_start):
            groups[TUESDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[TUESDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[TUESDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[TUESDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == WEDNESDAY:
        if calcs.is_morning(curr_start):
            groups[WEDNESDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[WEDNESDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[WEDNESDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[WEDNESDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == THURSDAY:
        if calcs.is_morning(curr_start):
            groups[THURSDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[THURSDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[THURSDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[THURSDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == FRIDAY:
        if calcs.is_morning(curr_start):
            groups[FRIDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[FRIDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[FRIDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[FRIDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == SATURDAY:
        if calcs.is_morning(curr_start):
            groups[SATURDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[SATURDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[SATURDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[SATURDAY][NIGHT].append(trips_list[trip])
    elif curr_start[0] == SUNDAY:
        if calcs.is_morning(curr_start):
            groups[SUNDAY][MORNING].append(trips_list[trip])
        elif calcs.is_day(curr_start):
            groups[SUNDAY][DAY].append(trips_list[trip])
        elif calcs.is_noon(curr_start):
            groups[SUNDAY][NOON].append(trips_list[trip])
        elif calcs.is_night(curr_start):
            groups[SUNDAY][NIGHT].append(trips_list[trip])
