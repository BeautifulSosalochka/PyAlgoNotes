import time


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited


def test_dfs():
    # список смежности
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    start = input("Введите начальную вершину: ")

    start_time = time.time()
    visited_recursive = dfs_recursive(graph, start)
    recursive_time = time.time() - start_time

    start_time = time.time()
    visited_iterative = dfs_iterative(graph, start)
    iterative_time = time.time() - start_time

    print(f"Рекурсивный DFS: {visited_recursive}")
    print(f"Итеративный DFS: {visited_iterative}")
    print(f"Время рекурсивного DFS: {recursive_time:.6f} секунд")
    print(f"Время итеративного DFS: {iterative_time:.6f} секунд")


if __name__ == "__main__":
    test_dfs()
