class ParcelTreeNode:
    def __init__(self, parcel_id):
        self.parcel_id = parcel_id
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def display_tree(node, level=0):
    print("  " * level + f"Parcel {node.parcel_id}")
    for child in node.children:
        display_tree(child, level + 1)

def create_parcel_tree():
    root = ParcelTreeNode("P001")
    
    parcel_0011 = ParcelTreeNode("P0011")
    parcel_0012 = ParcelTreeNode("P0012")
    
    parcel_00111 = ParcelTreeNode("P00111")
    parcel_00112 = ParcelTreeNode("P00112")
    
    root.add_child(parcel_0011)
    root.add_child(parcel_0012)
    
    parcel_0011.add_child(parcel_00111)
    parcel_0011.add_child(parcel_00112)
    
    return root

def main():
    root = create_parcel_tree()
    
    print("Parcel Hierarchy (Tree Structure):")
    display_tree(root)

if __name__ == "__main__":
    main()

#  alternative 2


import matplotlib.pyplot as plt
import networkx as nx

def create_parcel_hierarchy():
    G = nx.DiGraph()

    G.add_edges_from([
        ("P001", "P0011"), 
        ("P001", "P0012"),
        ("P002", "P0021"),
        ("P002", "P0022"),
        ("P0011", "P00111"),  
        ("P0011", "P00112"),
    ])

    return G

def visualize_parcel_hierarchy(G):
    pos = nx.spring_layout(G, seed=42) 

    plt.figure(figsize=(10, 8))  
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
    
    plt.title("Parcel Hierarchical Structure", fontsize=16)
    plt.show()

def main():
    G = create_parcel_hierarchy()

    visualize_parcel_hierarchy(G)

if __name__ == "__main__":
    main()
