from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

def test_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start = input("Введите начальную вершину: ")

    traversal_order = bfs(graph, start)

    print(f"Порядок обхода (BFS) от вершины {start}:")
    print(" -> ".join(traversal_order))


if __name__ == "__main__":
    test_bfs()
