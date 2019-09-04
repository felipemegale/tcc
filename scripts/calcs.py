from math import acos, sin, radians, cos
from datetime import datetime, timedelta


# this function returns the distance between the two given
# geographical coordinates in kilometers
def calc_dist(geoloc1, geoloc2):
    if geoloc1[0] == geoloc2[0] and geoloc1[1] == geoloc2[1]:
        return 0.0
    else:
        arg = sin(radians(geoloc2[0])) * sin(radians(geoloc1[0])) + cos(radians(
            geoloc2[0])) * cos(radians(geoloc1[0])) * cos(radians(geoloc1[1] - geoloc2[1]))
        if (-1 <= arg <= 1):
            return acos(arg) * 6371
        else:
            return 0.0


def calc_time_diff(time1, time2):
    datetime1 = datetime.strptime(time1, "%d/%m/%Y %H:%M")
    datetime2 = datetime.strptime(time2, "%d/%m/%Y %H:%M")

    diff = (datetime1 - datetime2)

    return int(diff.total_seconds()*1000)


def compatible_by(or_dest, timespan, max_dist, trip_a, trip_b):
    time_in_ms = timespan*3600*1000
    if or_dest == "origin":
        time_trip_a = trip_a[2]
        time_trip_b = trip_b[2]

        loc_trip_a = (float(trip_a[3]), float(trip_a[4]))
        loc_trip_b = (float(trip_b[3]), float(trip_b[4]))

    elif or_dest == "destination":
        time_trip_a = trip_a[5]
        time_trip_b = trip_b[5]

        loc_trip_a = (float(trip_a[6]), float(trip_a[7]))
        loc_trip_b = (float(trip_b[6]), float(trip_b[7]))

    else:
        return "You must choose 'origin' or 'destination' as comparison criterion"

    time_diff = abs(calc_time_diff(
        time_trip_a, time_trip_b))
    loc_diff = abs(calc_dist(
        loc_trip_a, loc_trip_b))

    if time_diff <= time_in_ms and loc_diff <= max_dist:
        return True
    return False
