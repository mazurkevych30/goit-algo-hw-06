import networkx as nx

def dijkstra(graph: nx, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attributes in graph[current_vertex].items():
            distance = distances[current_vertex] + attributes["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end

    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    if path:
        path.insert(0, start)

    return path, distances[end]
