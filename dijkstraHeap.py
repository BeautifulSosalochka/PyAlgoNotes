import heapq


def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def test_dijkstra():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start = input("Введите начальную вершину: ")

    distances = dijkstra(graph, start)

    print(f"Кратчайшие расстояния от вершины {start}:")
    for node, distance in distances.items():
        print(f"{node}: {distance if distance != float('inf') else 'недостижимо'}")


if __name__ == "__main__":
    test_dijkstra()
