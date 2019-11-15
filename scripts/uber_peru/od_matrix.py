import pandas as pd
import json
from calcs import get_districts_by_file, get_jsons_by_file, get_column


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

print("APPENDING DISTRICTS...")
# all districts list
for dist in en_districts:
    districts.append(dist)
for dist in st_districts:
    if dist not in districts:
        districts.append(dist)

districts.sort()
print("APPENDING DISTRICTS... OK")

print("CREATING IN_N_OUT AND MATRIX...")
in_n_out = {district: {'in': 0, 'out': 0} for district in districts}
matrix = [[0 for x in range(len(en_districts))]
          for y in range(len(st_districts))]
print("CREATING IN_N_OUT AND MATRIX... OK")

# OK terei uma nova matriz, onde as linhas sao out degree e as colunas sao in degreeß

# ai eu preciso ter na posicao i,j dessa matriz
# quantas viagens eu tenho que saem de um vertice de out degree X
# e chegam em um vertice de in degree Y

# agora, com essa matriz, eu nao preciso me preocupar com rotulos!!!

print("SORTING ST AND EN DISTRICTS...")
st_districts.sort()  # 46
en_districts.sort()  # 128
print("SORTING ST AND EN DISTRICTS... OK")

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

print("FINDING LARGEST IN AND OUT DEGREES...")
# get largest out degree and in degree
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

print("CREATING AND POPULATING MATRIX_INNOUT...")
# matrix with dimensions [out][in]
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

print("CALCULATING AMOUNT OF EDGES...")
for i in range(len(matrix_innout)):
    for j in range(len(matrix_innout[0])):
        edges += matrix_innout[i][j]
print("CALCULATING AMOUNT OF EDGES... OK")

print("CREATING AND POPULATING PROB_MATRIX...")
prob_matrix = [[0 for x in range(max_in+1)]
               for y in range(max_out+1)]

# calcula valores na matriz de probabilidades
for i in range(len(matrix_innout)):
    for j in range(len(matrix_innout[0])):
        prob_matrix[i][j] = matrix_innout[i][j]/edges
print("CREATING AND POPULATING PROB_MATRIX... OK")

print("CALCULATE PK1 AND PK2...")
# calcula Pk1
for row in prob_matrix:
    pk1.append(sum(row))

# calcula Pk2
for i in range(len(prob_matrix[0])):
    pk2.append(sum(get_column(prob_matrix, i)))
print("CALCULATE PK1 AND PK2... OK")

# calcular R(k1,k2) = k1*k2 * (P(k1,k2) - P(k1)*P(k2))
# mas quem sao k1 e k2? no exemplo da aula são os graus dos vertices
# só se eu converter o nome do distrito no indice dele na lista
# mas ai distritos com Z ou perto do Z terao R(k1,k2) maiores... (ou menores)

'''
como eu vou pegar k1 e k2:
k1 (coluna) eh o numero de arestas de saida
k2 (linha) eh o numero de arestas de chegada
'''
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
print(rk1k2)
