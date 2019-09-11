import networkx as nx
import matplotlib.pyplot as plt
import os


files = sorted(os.listdir("graph_adjlists"))
graph_names = ["0.5h\n0.5km", "0.5h\n1.0km", "0.5h\n2.0km", "1.0h\n0.5km",
               "1.0h\n1.0km", "1.0h\n2.0km", "2.0h\n0.5km", "2.0h\n1.0km", "2.0h\n2.0km"]
edges_origin = []
edges_destination = []

for file_name in files:
    file_path = "graph_adjlists/{}".format(file_name)

    graph = nx.read_adjlist(file_path)

    if "destination" in file_path:
        edges_destination.append(nx.number_of_edges(graph))
    else:
        edges_origin.append(nx.number_of_edges(graph))

plt.figure(figsize=(7.3, 5.5))
plt.bar(graph_names, edges_origin, width=0.4, color="xkcd:azure")
plt.title("Number of Edges - Combination by Origin")
plt.ylabel("Edges")
plt.xlabel("Combination")
plt.savefig("images/edges-origin.png")

plt.figure(figsize=(7.3, 5.5))
plt.bar(graph_names, edges_destination, width=0.4, color="xkcd:azure")
plt.title("Number of Edges - Combination by Destination")
plt.ylabel("Edges")
plt.xlabel("Combination")
plt.savefig("images/edges-destination.png")
