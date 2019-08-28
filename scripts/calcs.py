import math


def sin_rad(val):
    return math.sin(math.radians(val))


def cos_rad(val):
    return math.cos(math.radians(val))


# this function returns the distance between the two given
# geographical coordinates in kilometers
def calculate_distance_between_positions(lat1, lon1, lat2, lon2):
    return 6371 * math.acos(sin_rad(lat2)*sin_rad(lat1) + cos_rad(lat2)*cos_rad(lat1)*cos_rad(lon1-lon2))
