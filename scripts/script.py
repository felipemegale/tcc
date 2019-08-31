import calcs
import networkx as nx
import csv

graph_by_origin = nx.Graph()
graph_by_destination = nx.Graph()
trips = []
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
    trip_a = trips[i]
    trip_b = trips[j]

    i += 2
    j += 2
