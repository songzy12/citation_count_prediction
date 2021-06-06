import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edge('A', 'B')
G.add_edge('B', 'A')
G.add_edge('B', 'C')
G.add_edge('C', 'B')
G.add_edge('C', 'D')
G.add_edge('D', 'C')

pr = nx.pagerank(G)
print(pr)
