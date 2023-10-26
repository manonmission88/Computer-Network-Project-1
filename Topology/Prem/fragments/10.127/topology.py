import networkx as nx
import matplotlib.pyplot as plt
import ast
import itertools

'''
This python Script: 
reads routes.txt and creates a topology
'''

def get_colors(G):
    node_colors = {}
    color_iter = [(0/255.0, 0/255.0, 255/255.0), (255/255.0, 0/255.0, 0/255.0), (0/255.0, 255/255.0, 0/255.0), (255/255.0, 0/255.0, 255/255.0), (0/255.0, 255/255.0, 255/255.0), (127/255.0, 0/255.0, 255/255.0), (127/255.0, 0/255.0, 255/255.0), (255/255.0, 255/255.0, 0/255.0), (0/255.0, 102/255.0, 102/255.0)]
    l = len(color_iter)
    #print("Total colors = ",l)
    c = 0
    for node in G.nodes():
        node_colors[node] = color_iter[c]
        c += 1
        if c >= l:
            c = 0
    #print("node_colors")
    #print(node_colors)
    return node_colors

def topology(fname):
    G = nx.DiGraph()
    try:
        with open(fname, 'r') as file:
            lines = file.readlines()

            for line in lines:
                try:
                    result_list = ast.literal_eval(line)
                    result_list = [item.rstrip('\n') for item in result_list]

                    if len(result_list) == 0:
                        continue

                    if len(result_list) == 1:
                        G.add_node(result_list[0])

                    for i in range(len(result_list) - 1):
                        source = result_list[i]
                        dest = result_list[i + 1]
                        if source == dest:
                            continue
                        G.add_edge(source, dest)
                except ValueError:
                    print(f"Could not convert line {line} to list.")
    except FileNotFoundError:
        print("File not found.")
        
    return G

if __name__ == "__main__":
    try:
        G = topology("routes.txt")
        if G is None:
            print("Failed to create the graph.")
            exit(1)
        
        dict_colors = get_colors(G)

        edge_colors = list(dict_colors.values())

        plt.figure(figsize=(50, 50))
        pos = nx.spring_layout(G, seed=0, k=3, scale=5)

        nx.draw(G, pos, with_labels=False, node_size=1500, node_color=[(245/255.0, 250/255.0, 255/255.0)], edge_color=edge_colors, width=3, arrows=True, arrowsize=25)

        for node, (x, y) in pos.items():
            plt.text(x, y, node, fontsize=30, ha='center', va='center', color='black')
            #plt.text(x, y, node, fontsize=30, ha='center', va='center', color=font_colors.get(node, 'black'))

        plt.title("Network Topology from Traceroute Data")
        image_path = f"10.127.png"
        plt.savefig(image_path, dpi=300)
        plt.close()
        
        with open(f"10.127.md", "w") as md_file:
            print("Writing to the Markdown file...")
            md_file.write("# Building Network Topology\n")
            md_file.write(f"![Network Topology]({image_path})")
            print("Successfully written to topology_final.md")
    except Exception as e:
        print(f"An error occurred: {e}")