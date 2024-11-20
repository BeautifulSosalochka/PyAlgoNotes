from collections import defaultdict

def kosaraju(graph):
    def dfs_first_pass(node, visited, finish_order):
        stack = [node]
        visited.add(node)
        while stack:
            current = stack[-1]
            unvisited_neighbors = [n for n in graph[current] if n not in visited]
            if unvisited_neighbors:
                stack.append(unvisited_neighbors[0])
                visited.add(unvisited_neighbors[0])
            else:
                stack.pop()
                finish_order.append(current)

    def dfs_second_pass(node, visited, transposed_graph, component):
        stack = [node]
        visited.add(node)
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in transposed_graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    visited = set()
    finish_order = []
    for node in graph:
        if node not in visited:
            dfs_first_pass(node, visited, finish_order)

    transposed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)

    visited.clear()
    sccs = []
    while finish_order:
        node = finish_order.pop()
        if node not in visited:
            component = []
            dfs_second_pass(node, visited, transposed_graph, component)
            sccs.append(component)

    return sccs


def test_kosaraju():
    graph = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G']
    }

    sccs = kosaraju(graph)

    print("Компоненты сильной связности (SCC):")
    for i, scc in enumerate(sccs, 1):
        print(f"{i}: {scc}")


if __name__ == "__main__":
    test_kosaraju()
