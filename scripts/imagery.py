import networkx as nx
import pygraphviz as pgv


g = nx.read_adjlist("graph_adjlists/graph_by_origin_2_2.adjlist")
a = nx.nx_agraph.to_agraph(g)
a.layout(prog='dot')
print("finished layout")
a.draw("t1.png")
print("finished drawing")
