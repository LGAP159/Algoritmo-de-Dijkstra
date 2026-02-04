import heapq

def dijkstra(graph, start, goal):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]

    return distances[goal], path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

start_node = 'A'
goal_node = 'D'

shortest_distance, path = dijkstra(graph, start_node, goal_node)

print(f"Menor distância de {start_node} até {goal_node}: {shortest_distance}")
print(f"Caminho: {' -> '.join(path)}")
