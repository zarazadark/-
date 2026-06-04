import heapq
def dijkstra(graph, start_vertex):

   
    distances = {vertex: float("inf") for vertex in graph}
    distances[start_vertex] = 0

    
    previous_vertices = {vertex: None for vertex in graph}

   
    priority_queue = [(0, start_vertex)]

    while priority_queue:
       
        current_distance, current_vertex = heapq.heappop(priority_queue)

        
        if current_distance > distances[current_vertex]:
            continue

       
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

           
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
               
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices


def reconstruct_path(previous_vertices, start_vertex, end_vertex):
    
    path = []
    current_vertex = end_vertex

    
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]

    path.reverse()

   
    if path[0] == start_vertex:
        return path
    return []



if __name__ == "__main__":
   
    sample_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)],
    }

    start_node = "A"
    print(f"--- Расчет кратчайших путей от вершины '{start_node}' ---\n")

   
    shortest_paths, travel_history = dijkstra(sample_graph, start_node)

   
    for node in sample_graph:
        dist = shortest_paths[node]
        if dist == float("inf"):
            print(f"Вершина {node}: путь недостижим")
        else:
            full_path = reconstruct_path(travel_history, start_node, node)
            path_visual = " -> ".join(full_path)
            print(f"До вершины {node}: кратчайшее расстояние = {dist:2d} | Маршрут: {path_visual}")
