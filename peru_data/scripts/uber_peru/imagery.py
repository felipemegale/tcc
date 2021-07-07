import networkx as nx
import os
from time import strftime, localtime
import matplotlib.pyplot as plt


files = os.listdir("graph_adjlists")

for file_name in files:
    file_path = "graph_adjlists/{}".format(file_name)
    img_name = "{}png".format(file_name.split('adjlist')[0])

    print("{1} => reading file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    g = nx.read_adjlist(file_path)
    print("{1} => finished reading file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))

    print("{1} => started draw for file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    nx.draw(g, edge_color='blue', width=0.2, node_size=5, node_color='black')
    print("{1} => finished draw for file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))

    print("{1} => started drawing image {0}".format(
        img_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    plt.savefig(img_name, quality=50)
    print("{1} => finished drawing image {0}".format(
        img_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
