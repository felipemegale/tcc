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
