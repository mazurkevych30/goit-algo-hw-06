from algorithm.dijkstra import shortest_path
from task_1 import G

START_VERTEX = "Birmingham"
shortest_paths = {}

for end_vertex in G.nodes:
    if START_VERTEX != end_vertex:
        path, total_weight = shortest_path(G, START_VERTEX, end_vertex)
        shortest_paths[(START_VERTEX, end_vertex)] = (path, total_weight)

for city, (path, total_weight) in shortest_paths.items():
    print(f"Shortest path from {city[0]} to {city[1]}: {path}, Total weight: {total_weight}")
