import networkx as nx
import matplotlib.pyplot as plt
from scapy.all import traceroute, IP, UDP, sr1
from random import randint
import os

def parse_traceroute_file(fname):
    routers = []
    with open(fname, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "hops away" in line and ":" in line:
                router = line.split(":")[1].strip()

                # Exclude routers starting with 138.238 and greater
                parts = router.split(".")
                if parts[0] == "138" and int(parts[1]) >= 238:
                    continue

                if not router.startswith("138.238"):  # Exclude routers that start with 138.238
                    routers.append(router)
    if routers:  # Remove destination IP (last router in the list)
        routers.pop()
    return routers

def create_topology_graph(route):
    G = nx.Graph()
    for i in range(1, len(route)):
        G.add_edge(route[i-1], route[i])
    return G

if __name__ == "__main__":

    routers = parse_traceroute_file(f"c.txt")
    routers[0] = '10.26.96.1'

    # Create a graph topology
    G = create_topology_graph(routers)

    # Visualize the graph
    plt.figure(figsize=(12, 12))  # Increase figure size
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=8, width=3, edge_color="gray", node_shape='s')
    plt.title("Building Network Topology")
    #plt.tight_layout()  # Ensure content fits within the figure

    # Save the graph as an image
    image_path = f"c.png"
    plt.savefig(image_path, dpi=300)
    plt.close()

    # Write the image reference to a Markdown file
    with open("c.md", "w") as md_file:
        md_file.write("# Building Network Topology\n")
        md_file.write(f"![Network Topology]({image_path})")