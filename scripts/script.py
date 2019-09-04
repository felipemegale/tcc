import calcs
import networkx as nx
import matplotlib.pyplot as plt
import csv

trips = []
trips_part = []
line_no = 0
timespan = [0.5, 1, 2]
max_dist = [0.5, 1, 2]

with open('csv/uber_peru_2010_formatted_complete_fixed.csv') as trip_file:
    reader = csv.reader(trip_file, delimiter=";")

    # load to memory the trips from the file
    # also load a graph with nodes being trip IDs
    for row in reader:
        if line_no != 0:
            trips.append(row)
        line_no += 1

for time in timespan:
    for dist in max_dist:
        graph_by_origin = nx.Graph()
        graph_by_destination = nx.Graph()

        for trip in trips:
            graph_by_origin.add_node(trip[0])
            graph_by_destination.add_node(trip[0])

        for index_i in range(20):
            trip_a = trips[index_i]
            for index_j in range(index_i, 20):
                if index_i != index_j:
                    trip_b = trips[index_j]
                    # print(index_i, index_j)
                    if calcs.compatible_by("origin", time, dist, trip_a, trip_b):
                        graph_by_origin.add_edge(trip_a[0], trip_b[0])
                    elif calcs.compatible_by("destination", time, dist, trip_a, trip_b):
                        graph_by_destination.add_edge(trip_a[0], trip_b[0])

        nx.write_adjlist(
            graph_by_origin, "graph_by_origin_{}_{}.adjlist".format(str(time), str(dist)))
        nx.write_adjlist(graph_by_destination, "graph_by_destination_{}_{}.adjlist".format(
            str(time), str(dist)))
