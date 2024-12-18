from typing import List, Tuple

def bellman_ford(vertices: int, edges: List[Tuple[int, int, int]], source: int) -> List[int]:
    """
    Bellman-Ford algorithm to find the shortest paths from a single source node to all other nodes.

    :param vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is represented as (u, v, weight)
    :param source: The source vertex
    :return: List of shortest distances from the source to each vertex
    """
    distances = [float('inf')] * vertices
    distances[source] = 0

    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances


def generate_large_test_case(vertices: int, edges_count: int) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Generate a large test case for the Bellman-Ford algorithm.

    :param vertices: Number of vertices
    :param edges_count: Number of edges
    :return: A tuple of source vertex and a list of edges
    """
    import random
    edges = []

    for i in range(vertices - 1):
        weight = random.randint(1, 100)
        edges.append((i, i + 1, weight))

    while len(edges) < edges_count:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v:
            weight = random.randint(-50, 100)

            edges.append((u, v, weight))
            try:
                bellman_ford(vertices, edges, 0)
            except ValueError:
                edges.pop()

    source = random.randint(0, vertices - 1)
    return source, edges


def test_bellman_ford():
    """
    Test the Bellman-Ford implementation with predefined and random test cases.
    """
    vertices = 5
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 0, 2),
        (4, 3, 7)
    ]
    source = 0
    expected_distances = [0, 2, 7, 4, -2]

    assert bellman_ford(vertices, edges, source) == expected_distances, "Test case 1 failed"

    vertices = 100
    edges_count = 500
    source, edges = generate_large_test_case(vertices, edges_count)
    try:
        distances = bellman_ford(vertices, edges, source)
        print("Random test case passed.")
    except ValueError as e:
        print("Random test case failed: ", e)


if __name__ == "__main__":
    print("Running predefined test case...")
    test_bellman_ford()

    print("Generating large test case...")
    vertices = 1000
    edges_count = 10000
    source, edges = generate_large_test_case(vertices, edges_count)

    print("Running Bellman-Ford on large test case...")
    try:
        distances = bellman_ford(vertices, edges, source)
        print("Shortest distances from source:", distances[:10], "...")
    except ValueError as e:
        print(e)
