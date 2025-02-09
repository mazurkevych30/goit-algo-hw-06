import networkx as nx
import matplotlib.pyplot as plt

from data import cities, routes

G = nx.Graph()

G.name = "City connection"
G.add_nodes_from(cities)
G.add_weighted_edges_from(routes)

def main():
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print("Degree of each node:")
    for city in G.nodes():
        print(f"{city}: {G.degree(city)}")

    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2500,
        font_size=10,
        font_weight='bold',
        edge_color='gray'
        )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title("Cities Network Graph")
    plt.show()

if __name__ == "__main__":
    main()
