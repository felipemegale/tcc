import csv
import math


def sin_rad(val):
    return math.sin(math.radians(val))


def cos_rad(val):
    return math.cos(math.radians(val))


def calculate_distance_between_positions(lat1, lon1, lat2, lon2):
    return 6371 * math.acos(sin_rad(lat2)*sin_rad(lat1) + cos_rad(lat2)*cos_rad(lat1)*cos_rad(lon1-lon2))


print(calculate_distance_between_positions(
    -12.13983536, -77.02355957, -12.13874817, -76.99536133))
