import pandas as pd
import numpy as np
import json
from calcs import get_districts_by_file, get_jsons_by_file, get_column
from time import sleep
from math import sqrt


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

print("CREATING IN_N_OUT AND MATRIX...")
in_n_out = {district: {'in': 0, 'out': 0} for district in districts}
matrix = [[0 for x in range(len(en_districts))]
          for y in range(len(st_districts))]
print("CREATING IN_N_OUT AND MATRIX... OK")
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
    matrix[st_districts.index(start)][en_districts.index(end)] += 1
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

print("CREATING AND POPULATING MATRIX_INNOUT...")
matrix_innout = [[0 for x in range(max_in+1)] for y in range(max_out+1)]
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
    out_degree = in_n_out[start]['out']
    in_degree = in_n_out[end]['in']
    matrix_innout[out_degree][in_degree] += 1
print("CREATING AND POPULATING MATRIX_INNOUT... OK")
sleep(0.5)

print("CALCULATING AMOUNT OF EDGES...")
for row in matrix_innout:
    edges += sum(row)
print("CALCULATING AMOUNT OF EDGES... OK")
sleep(0.5)

print("CREATING AND POPULATING PROB_MATRIX...")
prob_matrix = [[0 for x in range(max_in+1)] for y in range(max_out+1)]
for i in range(len(matrix_innout)):
    for j in range(len(matrix_innout[0])):
        prob_matrix[i][j] = matrix_innout[i][j]/edges
print("CREATING AND POPULATING PROB_MATRIX... OK")
sleep(0.5)

print("CALCULATING PK1 AND PK2...")
for row in prob_matrix:
    pk1.append(sum(row))
for i in range(len(prob_matrix[0])):
    pk2.append(sum(get_column(prob_matrix, i)))
print("CALCULATING PK1 AND PK2... OK")
sleep(0.5)

print("CALCULATING RK1K2...")
rk1k2 = 0
for i in range(len(matrix_innout)):
    for j in range(len(matrix_innout[0])):
        k1 = j
        k2 = i
        pk1k2 = prob_matrix[i][j]
        _pk1 = pk1[i]
        _pk2 = pk2[j]
        rk1k2 += k1*k2*(pk1k2 - _pk1*_pk2)
print("CALCULATING RK1K2... OK")
sleep(0.5)

print("CALCULATING OUT DEGREE AVERAGE...")
avg_sum = 0
for i in range(len(matrix_innout)):
    avg_sum += sum(matrix_innout[i])*i
out_avg = avg_sum/edges
print("CALCULATING OUT DEGREE AVERAGE... OK")
sleep(0.5)

print("CALCULATING IN DEGREE AVERAGE...")
avg_sum = 0
transposed = np.transpose(matrix_innout)
for i in range(len(transposed)):
    avg_sum += sum(transposed[i])*i
in_avg = avg_sum/edges
print("CALCULATING IN DEGREE AVERAGE... OK")
sleep(0.5)

print("CALCULATING OUT DEGREE VARIANCE...")
var_sum = 0
for i in range(len(matrix_innout)):
    var_sum += sum(matrix_innout[i])*(i - out_avg)**2
out_var = var_sum/edges
print("CALCULATING OUT DEGREE VARIANCE... OK")
sleep(0.5)

print("CALCULATING IN DEGREE VARIANCE...")
var_sum = 0
for i in range(len(transposed)):
    var_sum += sum(transposed[i])*(i - in_avg)**2
in_var = var_sum/edges
print("CALCULATING IN DEGREE VARIANCE... OK")
sleep(0.5)

print("CALCULATING OUT DEGREE STD DEVIATION...")
out_std_dev = sqrt(out_var)
print("CALCULATING OUT DEGREE STD DEVIATION... OK")
sleep(0.5)

print("CALCULATING IN DEGREE STD DEVIATION...")
in_std_dev = sqrt(in_var)
print("CALCULATING IN DEGREE STD DEVIATION... OK")
sleep(0.5)

print("CALCULATING ASSORTATIVITY...")
assortativity = 1/(in_std_dev*out_std_dev) * rk1k2
print("CALCULATING ASSORTATIVITY... OK", end="\n\n")
print(assortativity, end="\n\n")

print("RANKING OUT DEGREES...")
out_values = [in_n_out[dist]['out'] for dist in in_n_out]
out_sort = [item for item in out_values]
out_sort.sort()
out_rank = [out_sort.index(item) for item in out_values]
print("RANKING OUT DEGREES... OK")
sleep(0.5)

print("RANKING IN DEGREES...")
in_values = [in_n_out[dist]['in'] for dist in in_n_out]
in_sort = [item for item in in_values]
in_sort.sort()
in_rank = [in_sort.index(item) for item in in_values]
print("RANKING IN DEGREES... OK")
sleep(0.5)

print("CALCULATING DIFFERENCE BETWEEN IN RANK AND OUT RANK...")

print("CALCULATING DIFFERENCE BETWEEN IN RANK AND OUT RANK... OK")
sleep(0.5)
