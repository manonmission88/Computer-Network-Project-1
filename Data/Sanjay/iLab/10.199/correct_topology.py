import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os
import ast

def topology(fname):
    G = nx.DiGraph()

    with open(fname, 'r') as file:

        lines = file.readlines()

        for line in lines:
            print(line)

            result_list = ast.literal_eval(line)
            result_list = [item.rstrip('\n') for item in result_list]

            if len(result_list) == 0:
                continue

            if len(result_list) == 1:
                G.add_node(result_list[0])

            for i in range(len(result_list)-1):
                source = result_list[i]
                dest = result_list[i+1]
                if source == dest:
                    continue
                G.add_edge(source, dest)

    return G

if __name__ == "__main__":
    
    G = topology("routes.txt")

    # Visualize the graph
    plt.figure(figsize=(50, 50))  # Increase figure size
    pos = nx.spring_layout(G, seed=0, k=3) # k=distance between nodes
    #pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="neato")  # you can also try "dot", "twopi", "circo", etc.
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightgreen', font_color="darkred", font_size=30, edge_color="grey", width=2)
    plt.title("Network Topology from Traceroute Data")
    # Save the plot to a PNG file
    image_path = f"final.png"
    plt.savefig(image_path, dpi=300)
    plt.close()
    # Write the image reference to a Markdown file
    with open(f"final.md", "w") as md_file:
        md_file.write("# Building Network Topology\n")
        md_file.write(f"![Network Topology]({image_path})")