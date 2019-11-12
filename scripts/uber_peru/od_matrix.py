import pandas as pd
import json
import networkx as nx


districts = []
st_districts = []
en_districts = []

with open("osm_start.out") as start:
    st_jsons = [json.loads(line) for line in start]
    
    for i in range(0, len(st_jsons)):
        if "city" in st_jsons[i]["address"]:
            if st_jsons[i]["address"]["city"] not in st_districts:
                st_districts.append(st_jsons[i]["address"]["city"])
        elif "town" in st_jsons[i]["address"]:
            if st_jsons[i]["address"]["town"] not in st_districts:
                st_districts.append(st_jsons[i]["address"]["town"])
        elif "village" in st_jsons[i]["address"]:
            if st_jsons[i]["address"]["village"] not in st_districts:
                st_districts.append(st_jsons[i]["address"]["village"])

    with open("osm_end.out") as end:
        en_jsons = [json.loads(line) for line in end]

        for i in range(0, len(en_jsons)):
            if "city" in en_jsons[i]["address"]:
                if en_jsons[i]["address"]["city"] not in en_districts:
                    en_districts.append(en_jsons[i]["address"]["city"])
            elif "town" in en_jsons[i]["address"]:
                if en_jsons[i]["address"]["town"] not in en_districts:
                    en_districts.append(en_jsons[i]["address"]["town"])
            elif "village" in en_jsons[i]["address"]:
                if en_jsons[i]["address"]["village"] not in en_districts:
                    en_districts.append(en_jsons[i]["address"]["village"])

        # all districts list
        for dist in en_districts:
            districts.append(dist)
        for dist in st_districts:
            if dist not in districts:
                districts.append(dist)

        matrix = [[0 for x in range(len(en_districts))] for y in range(len(st_districts))]
        st_districts.sort()
        en_districts.sort()
        
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
        
        # for row in matrix:
        #     print(row)

        # od = nx.Graph()
        # od.add_nodes_from(districts)