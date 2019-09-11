import networkx as nx
import matplotlib.pyplot as plt
import os
import collections


files = sorted(os.listdir("graph_adjlists"))
graph_names = ["0.5_0.5", "0.5_1.0", "0.5_2.0", "1.0_0.5",
               "1.0_1.0", "1.0_2.0", "2.0_0.5", "2.0_1.0", "2.0_2.0"]

for i in range(int(len(files)/2)):
    destination = files[i]
    origin = files[i+9]

    g_destination = nx.read_adjlist("graph_adjlists/{}".format(destination))
    g_origin = nx.read_adjlist("graph_adjlists/{}".format(origin))

    dest_degrees = sorted([d for n, d in g_destination.degree()], reverse=True)
    dest_degrees_count = collections.Counter(dest_degrees)
    dest_deg, dest_cnt = zip(*dest_degrees_count.items())

    orig_degrees = sorted([d for n, d in g_origin.degree()], reverse=True)
    orig_degrees_count = collections.Counter(orig_degrees)
    orig_deg, orig_cnt = zip(*orig_degrees_count.items())

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4.5))
    ax[0].set_title("By Origin")
    ax[0].set_xlabel("Node Degrees")
    ax[0].set_ylabel("Node Count")
    ax[0].plot(orig_deg, orig_cnt, 'go')
    ax[1].set_title("By Destination")
    ax[1].set_xlabel("Node Degrees")
    ax[1].plot(dest_deg, dest_cnt, 'r^')
    plt.suptitle("Degree Distribution")
    plt.savefig("images/degrees_{}.png".format(graph_names[i]))
