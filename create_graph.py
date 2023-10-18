import networkx as nx
import matplotlib.pyplot as plt
from connections import connections

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from(connections)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=2000)
nx.draw_networkx_edges(G, pos, width=2, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
plt.axis('off')
plt.show()
