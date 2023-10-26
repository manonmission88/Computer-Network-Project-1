import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

def graph_trace(fname):
    G = nx.DiGraph()
    start = None
    with open(fname, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "hops away" in line and ":" in line:
                ip = line.split(":")[1].strip()
                if start == None:
                    start = ip
                    G.add_node(start)
                else:
                    dest = ip
                    G.add_edge(start, dest)
                    start = ip
            elif "STOP" in line:
                break
            else:
                start = None
                continue
    return G

if __name__ == "__main__":
    #for i in range(0, 6):
    G = graph_trace("all.txt")
    # Visualize the graph
    plt.figure(figsize=(50, 50))  # Increase figure size
    pos = nx.spring_layout(G, seed=0, k=2) # k=distance between nodes
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_color="darkred", font_size=30, edge_color="grey", width=1)
    plt.title("Network Topology from Traceroute Data")
    # Save the plot to a PNG file
    image_path = f"all0k2.png"
    plt.savefig(image_path, dpi=300)
    plt.close()
    # Write the image reference to a Markdown file
    with open(f"all.md", "w") as md_file:
        md_file.write("# Building Network Topology\n")
        md_file.write(f"![Network Topology]({image_path})")