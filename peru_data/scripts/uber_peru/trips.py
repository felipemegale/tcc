import csv
import json

'''
journey_idunique journey id
user_idunique user id
driver_idunique driver id
taxi_idunique taxt id
icontype of rider
start_typetype or start like as asap, reserved or delayed
start_atrider start at
start_latrider start at latitude
start_lonrider start at longitude
end_atrider end at
end_latrider end at latitude
end_lonrider end at longitude
end_statetype of end state
driver_start_latdriver start at latitude
driver_start_londriver start at longitude
arrived_atdriver arrived time
currencytype of currency
priceprice of rider
price_distanceprice by distance
price_durationprice by duration
distancedistance of rider
durationduration of rider
costcost of rider
cost_distancecost by distance
cost_durationcost by duration
sourcesource type of user
driver_scorescore of driver
rider_scorescore of rider
'''


'''
journey_id;
user_id;
driver_id;
taxi_id;
icon;
start_type;
start_at;
start_lat;
start_lon;
end_at;
end_lat;
end_lon;
end_state;
driver_start_lat;
driver_start_lon;
arrived_at;
currency;
price;
price_distance;
price_duration;
distance;
duration;
cost;
cost_distance;
cost_duration;
source;
driver_score;
rider_score
'''


class Trip:
    def __init__(self, start_at, start_lat, start_lon, end_at, end_lat, end_lon):
        self.start_at = start_at
        self.start_lat = start_lat
        self.start_lon = start_lon
        self.end_at = end_at
        self.end_lat = end_lat
        self.end_lon = end_lon

    def to_string(self):
        return '{0},{1},{2},{3},{4},{5}'.format(self.start_at, self.start_lat, self.start_lon, self.end_at, self.end_lat, self.end_lon)


lineNo = 0
trips = {}
header = []

with open('uber_peru_head_complete.csv') as in_file:
    reader = csv.reader(in_file, delimiter=';')

    for row in reader:
        if (lineNo != 0):
            try:
                trips[row[1]].append(
                    Trip(row[6], row[7], row[8], row[9], row[10], row[11]))
            except:
                trips[row[1]] = []
                trips[row[1]].append(
                    Trip(row[6], row[7], row[8], row[9], row[10], row[11]))
        lineNo += 1

for trip in trips:
    print(trip)
    for x in trips[trip]:
        print(x.to_string())
