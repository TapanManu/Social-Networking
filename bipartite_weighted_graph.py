import networkx as nx
from networkx.algorithms import bipartite

B = nx.Graph()
B.add_edges_from([('A', 'G'),('A','I'), ('B','H'), ('C', 'G'), ('C', 'I'),('D', 'H'), ('E', 'I'), ('F', 'G'), ('F', 'J')])
X1 = set(['A', 'B', 'C', 'D', 'E', 'F'])
G=bipartite.weighted_projected_graph(B,X1)
G.edge['A']['C']['weight']
#answer is 2
