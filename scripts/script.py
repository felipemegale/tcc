import calcs
import networkx as nx
import matplotlib.pyplot as plt
import csv

graph_by_origin = nx.Graph()
graph_by_destination = nx.Graph()
trips = []
trips_part = []
line_no = 0
i = 0
j = 1

with open('csv/uber_peru_2010_formatted_complete_fixed.csv') as trip_file:
    reader = csv.reader(trip_file, delimiter=";")

    # load to memory the trips from the file
    # also load a graph with nodes being trip IDs
    for row in reader:
        if line_no != 0:
            trips.append(row)
            graph_by_origin.add_node(row[0])
            graph_by_destination.add_node(row[0])
        line_no += 1

for index in range(0, 100):
    trips_part.append(trips[index])

for a in range(len(trips_part)):
    trip_a = trips_part[i]
    j = i + 1
    for b in range(i, len(trips_part)-1):
        trip_b = trips_part[j]
        if calcs.compatible_by("origin", trip_a, trip_b):
            graph_by_origin.add_edge(trip_a[0], trip_b[0])
        elif calcs.compatible_by("destination", trip_a, trip_b):
            graph_by_destination.add_edge(trip_a[0], trip_b[0])
        j += 1
    i += 1

# for a in range(len(trips)):
#     trip_a = trips[i]
#     j = i + 1
#     for b in range(i, len(trips)-1):
#         trip_b = trips[j]
#         if calcs.compatible_by("origin", trip_a, trip_b):
#             graph_by_origin.add_edge(trip_a[0], trip_b[0])
#         elif calcs.compatible_by("destination", trip_a, trip_b):
#             graph_by_destination.add_edge(trip_a[0], trip_b[0])
#         j += 1
#     i += 1

print("finished")
