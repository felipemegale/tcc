import pandas as pd
import json
import networkx as nx
from calcs import get_districts_by_file, get_jsons_by_file, get_column


districts = []
pk1 = []
pk2 = []
edges = 0

# graph = nx.DiGraph()
st_districts = get_districts_by_file("osm_start.out")
st_jsons = get_jsons_by_file("osm_start.out")
en_districts = get_districts_by_file("osm_end.out")
en_jsons = get_jsons_by_file("osm_end.out")

# all districts list
for dist in en_districts:
    districts.append(dist)
for dist in st_districts:
    if dist not in districts:
        districts.append(dist)

districts.sort()
# graph.add_nodes_from(districts)

matrix = [[0 for x in range(len(en_districts))]
          for y in range(len(st_districts))]

st_districts.sort()  # 46
en_districts.sort()  # 128

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

    # if graph.has_edge(start, end):
    #     graph[start][end]['weight'] = graph.get_edge_data(start, end)[
    #         'weight']+1
    # else:
    #     graph.add_edge(start, end, weight=1)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        edges += matrix[i][j]

prob_matrix = [[0 for x in range(len(en_districts))]
               for y in range(len(st_districts))]

# calcula valores na matriz de probabilidades
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        prob_matrix[i][j] = matrix[i][j]/edges

# calcula Pk1
for row in prob_matrix:
    pk1.append(sum(row))

# calcula Pk2
for i in range(len(prob_matrix[0])):
    pk2.append(sum(get_column(prob_matrix, i)))

# calcular R(k1,k2) = k1*k2 * (P(k1,k2) - P(k1)*P(k2))
# mas quem sao k1 e k2? no exemplo da aula são os graus dos vertices
# só se eu converter o nome do distrito no indice dele na lista
# mas ai distritos com Z ou perto do Z terao R(k1,k2) maiores... (ou menores)
