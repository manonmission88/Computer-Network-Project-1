import networkx as nx
import matplotlib.pyplot as plt

def parse_traceroute_file(filename):
    routers = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "hops away" in line and ":" in line:
                router = line.split(":")[1].strip()

                # Exclude routers starting with 138.238 and greater
                parts = router.split(".")
                if parts[0] == "66":
                    continue 
                if int(parts[0]) > 138:
                    continue

                routers.append(router)
    if routers:  # Remove destination IP (last router in the list)
        routers.pop()
    return routers

def create_topology_graph(route):
    G = nx.Graph()
    for i in range(1, len(route)):
        G.add_edge(route[i-1], route[i])
    return G

# Extract routers from the file
routers = parse_traceroute_file('/Users/manishnewray/Computer-Network-Project-1-1/Data/Manish/UglSubnet26/ugl_sn26.txt')

# Create a graph topology
G = create_topology_graph(routers)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightgreen', font_color="darkred", font_size=30, edge_color="grey", width=2)
plt.title("Building Network Topology")

# Save the graph as an image
image_path = "/Users/manishnewray/Computer-Network-Project-1-1/Data/Manish/UglSubnet26/ugl_sn.png"
plt.savefig(image_path)
plt.close()


with open("/Users/manishnewray/Computer-Network-Project-1-1/Data/Manish/UglSubnet26/ugl.md", "a") as md_file:
    md_file.write("Updated Ugl Toplogy Excluding Public")
    md_file.write(f"![Network Topology]({image_path})")