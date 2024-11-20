import heapq

"""
Введите начальную вершину: A
Введите конечную вершину: D
Кратчайшее расстояние от A до D: 4
Путь: A -> B -> C -> D

Введите начальную вершину: A
Введите конечную вершину: A
Кратчайшее расстояние от A до A: 0
Путь: A
"""


def dijkstra(graph, start, end):
    queue = [(0, start)]  # (расстояние, вершина)
    distances = {start: 0}  # Расстояния от начальной вершины
    previous_nodes = {start: None}  # Для восстановления пути

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return distances[end], path

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return float("inf"), []  # Если путь не найден


def test_dijkstra():
    # Пример графа в виде списка смежности
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
    }

    start = input("Введите начальную вершину: ")
    end = input("Введите конечную вершину: ")

    distance, path = dijkstra(graph, start, end)

    if path:
        print(f"Кратчайшее расстояние от {start} до {end}: {distance}")
        print(f"Путь: {' -> '.join(path)}")
    else:
        print(f"Путь от {start} до {end} не существует.")


if __name__ == "__main__":
    test_dijkstra()
