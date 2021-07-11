import networkx as nx
import matplotlib.pyplot as plt
import os


files = sorted(os.listdir("graph_adjlists/space"))
graph_names = ["0.5km", "1.0km", "2.0km"]
densities_origin = []
densities_destination = []

for file_name in files:
    file_path = "graph_adjlists/space/{}".format(file_name)

    graph = nx.read_adjlist(file_path)

    if "destination" in file_path:
        densities_destination.append(nx.density(graph))
    else:
        densities_origin.append(nx.density(graph))

plt.figure(figsize=(7.3, 5.5))
plt.bar(graph_names, densities_origin, width=0.4, color="xkcd:azure")
plt.title("Densities - Combination by Origin")
plt.ylabel("Density")
plt.xlabel("Combination")
plt.savefig("images/densities-origin-space.png")

plt.figure(figsize=(7.3, 5.5))
plt.bar(graph_names, densities_destination, width=0.4, color="xkcd:azure")
plt.title("Densities - Combination by Destination")
plt.ylabel("Density")
plt.xlabel("Combination")
plt.savefig("images/densities-destination-space.png")
