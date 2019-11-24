import pandas as pd
import numpy as np
import json
from calcs import get_districts_by_file, get_jsons_by_file, get_column
from time import sleep


districts = []
pk1 = []
pk2 = []
edges = 0

print("LOADING FILES...")
st_districts = get_districts_by_file("osm_start.out")
st_jsons = get_jsons_by_file("osm_start.out")
en_districts = get_districts_by_file("osm_end.out")
en_jsons = get_jsons_by_file("osm_end.out")
print("LOADING FILES... OK")
sleep(0.5)

print("APPENDING DISTRICTS...")
for dist in en_districts:
    districts.append(dist)
for dist in st_districts:
    if dist not in districts:
        districts.append(dist)
districts.sort()
print("APPENDING DISTRICTS... OK")
sleep(0.5)

print("CREATING IN_N_OUT...")
in_n_out = {district: {'in': 0, 'out': 0} for district in districts}
print("CREATING IN_N_OUT... OK")
sleep(0.5)

print("SORTING ST AND EN DISTRICTS...")
st_districts.sort()  # 46
en_districts.sort()  # 128
print("SORTING ST AND EN DISTRICTS... OK")
sleep(0.5)

print("ADDING INFO TO IN_N_OUT AND MATRIX...")
for i in range(len(st_jsons)):
    if "city" in st_jsons[i]["address"]:
        start = st_jsons[i]["address"]["city"]
    elif "town" in st_jsons[i]["address"]:
        start = st_jsons[i]["address"]["town"]
    elif "village" in en_jsons[i]["address"]:
        start = st_jsons[i]["address"]["village"]
    if "city" in en_jsons[i]["address"]:
        end = en_jsons[i]["address"]["city"]
    elif "town" in en_jsons[i]["address"]:
        end = en_jsons[i]["address"]["town"]
    elif "village" in en_jsons[i]["address"]:
        end = en_jsons[i]["address"]["village"]
    in_n_out[start]['out'] += 1
    in_n_out[end]['in'] += 1
print("ADDING INFO TO IN_N_OUT AND MATRIX... OK")
sleep(0.5)

print("FINDING LARGEST IN AND OUT DEGREES...")
max_out = 0
max_in = 0
for item in in_n_out:
    tmp_out = in_n_out[item]['out']
    tmp_in = in_n_out[item]['in']
    if tmp_out > max_out:
        max_out = tmp_out
    if tmp_in > max_in:
        max_in = tmp_in
print("FINDING LARGEST IN AND OUT DEGREES... OK")
sleep(0.5)

print("SORTING IN_N_OUT DICTIONARY...")
sorted_dict = sorted(in_n_out.items(), key=lambda x: x[1]['out'], reverse=True)
print("SORTING IN_N_OUT DICTIONARY... OK")
sleep(0.5)

for i in range(0, 5):
    print(sorted_dict[i])
