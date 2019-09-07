import networkx as nx
import os
from time import strftime, localtime


files = os.listdir("graph_adjlists")

for file_name in files:
    file_path = "graph_adjlists/{}".format(file_name)
    img_name = "{}png".format(file_name.split('adjlist')[0])

    print("{1} => reading file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    g = nx.read_adjlist(file_path)
    a = nx.nx_agraph.to_agraph(g)
    print("{1} => finished reading file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))

    print("{1} => started layout for file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    a.layout()
    print("{1} => finished layout for file {0}".format(
        file_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))

    print("{1} => started drawing image {0}".format(
        img_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
    a.draw(img_name)
    print("{1} => finished drawing image {0}".format(
        img_name, strftime("%Y-%m-%d %H:%M:%S", localtime())))
