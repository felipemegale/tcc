from math import acos, sin, radians, cos
from datetime import datetime, timedelta


# this function returns the distance between the two given
# geographical coordinates in kilometers
def calculate_distance_between_positions(geoloc1, geoloc2):
    if geoloc1[0] == geoloc2[0] and geoloc1[1] == geoloc2[1]:
        return 0.0
    return acos(sin(radians(geoloc2[0])) * sin(radians(geoloc1[0])) + cos(radians(geoloc2[0])) * cos(radians(geoloc1[0])) * cos(radians(geoloc1[1] - geoloc2[1]))) * 6371


def calculate_time_difference_in_milliseconds(time1, time2):
    datetime1 = datetime.strptime(time1, "%d/%m/%Y %H:%M")
    datetime2 = datetime.strptime(time2, "%d/%m/%Y %H:%M")

    diff = (datetime1 - datetime2)

    return int(diff.total_seconds()*1000)


def compatible_by_origin(trip_a, trip_b):
    start_time_trip_a = trip_a[2]
    start_time_trip_b = trip_b[2]

    start_loc_trip_a = (trip_a[3], trip_a[4])
    start_loc_trip_b = (trip_b[3], trip_b[4])

    start_time_diff = calculate_time_difference_in_milliseconds(
        start_time_trip_a, start_time_trip_b)
    start_loc_dist = calculate_distance_between_positions(
        start_loc_trip_a, start_loc_trip_b)

    if start_time_diff <= 1200000 and start_loc_dist <= 1.5:
        return True
    return False
