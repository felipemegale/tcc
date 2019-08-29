import math
from datetime import datetime, timedelta


def sin_rad(val):
    return math.sin(math.radians(val))


def cos_rad(val):
    return math.cos(math.radians(val))


# this function returns the distance between the two given
# geographical coordinates in kilometers
def calculate_distance_between_positions(geo_loc_1, geo_loc_2):
    return 6371 * math.acos(sin_rad(geo_loc_2[0])*sin_rad(geo_loc_1[0]) + cos_rad(geo_loc_2[0])*cos_rad(geo_loc_1[0])*cos_rad(geo_loc_1[1]-geo_loc_2[1]))


def calculate_time_difference_in_milliseconds(time1, time2):
    datetime1 = datetime.strptime(time1, "%d/%m/%Y %H:%M")
    datetime2 = datetime.strptime(time2, "%d/%m/%Y %H:%M")

    diff = (datetime1 - datetime2)

    return int(diff.total_seconds()*1000)

def compare_trips(trip_a, trip_b):
    start_time_trip_a = trip_a[2]
    end_time_trip_a = trip_a[5]
    start_time_trip_b = trip_b[2]
    end_time_trip_b = trip_b[5]

    start_loc_trip_a = (trip_a[3], trip_a[4])
    end_loc_trip_a = (trip_a[6], trip_a[7])
    start_loc_trip_b = (trip_b[3], trip_b[4])
    end_loc_trip_b = (trip_b[6], trip_b[7])

    start_time_diff = calculate_time_difference_in_milliseconds(start_time_trip_a, start_time_trip_b)
    end_time_diff = calculate_time_difference_in_milliseconds(end_time_trip_a, end_time_trip_b)

    start_loc_dist = calculate_distance_between_positions(start_loc_trip_a, start_loc_trip_b)
    end_loc_dist = calculate_distance_between_positions(end_loc_trip_a, end_loc_trip_b)

