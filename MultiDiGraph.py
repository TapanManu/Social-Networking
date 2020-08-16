import networkx as nx

G=nx.MultiDiGraph()

G.add_edge('John', 'Ana', weight= 3, relation = 'siblings')
G.add_edge('Ana', 'David', weight= 4, relation = 'cousins')
G.add_edge('Ana', 'Bob', weight= 1, relation = 'friends')
G.add_edge('Ana', 'Bob', weight= 1, relation = 'neighbors')

print( G.edge['Bob']['Ana'][1]['relation'] )
