import networkx as nx
import matplotlib.pyplot as plt

# Initialize a directed graph
G = nx.DiGraph()

# Define a set of IP addresses to include in the network graph
ip_addresses_to_include = {"10.78.96.1", "10.199.4.249", "10.199.2.14", "10.199.2.2", "10.199.4.249", "138.238.3.13", "66.44.94.195", '10.199.1.69', '10.199.4.90', '10.199.1.16', '10.199.1.134', '10.199.2.146', '10.199.2.80', '10.199.3.126', '10.199.3.29', '10.199.3.4', '10.199.3.153', '10.199.2.239', '10.199.4.55', '10.199.2.123', '10.199.2.187', '10.199.3.158', '10.199.1.110', '10.199.3.37', '10.199.1.212', '10.199.2.13', '10.199.3.30', '10.199.3.132', '10.199.3.209'}

# Read data from the text file
with open("sanjay_location.txt", "r") as file:
    lines = file.read().splitlines()

current_ip = None

for line in lines:
    if line.startswith("For ip addresses") or "hops away" in line:
        current_ip = line.split()[-1]
        if current_ip in ip_addresses_to_include:
            G.add_node(current_ip)

# Draw the network graph
pos = nx.spring_layout(G, seed=42)  # You can change the layout algorithm as needed

plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_size=500, node_color="black", font_size=10, font_color="black", arrowsize=20, arrows=True)
plt.title("Network Topology")
plt.show()
