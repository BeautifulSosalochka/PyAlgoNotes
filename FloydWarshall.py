import sys

def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of nodes in a weighted graph.

    :param graph: A 2D list where graph[i][j] represents the weight of the edge
                  from node i to node j (float('inf') if no edge exists).
    :return: A 2D list representing shortest path distances between all pairs.
    """
    num_vertices = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph

    for k in range(num_vertices):
        print(f"Processing vertex {k}...")
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance to the shortest possible path via vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        print(f"Distance matrix after processing vertex {k}:")
        for row in dist:
            print(row)

    return dist

def test_floyd_warshall():
    """
    Tests the Floyd-Warshall implementation with predefined graphs.
    """
    inf = float('inf')

    # Test graph 1
    graph1 = [
        [0, 3, inf, inf],
        [2, 0, inf, 4],
        [inf, 1, 0, 5],
        [inf, inf, 2, 0]
    ]

    expected_result1 = [
        [0, 3, 7, 7],
        [2, 0, 6, 4],
        [3, 1, 0, 5],
        [5, 3, 2, 0]
    ]

    result1 = floyd_warshall(graph1)
    if result1 != expected_result1:
        print("Test failed for graph1!")
        print("Expected:")
        for row in expected_result1:
            print(row)
        print("Got:")
        for row in result1:
            print(row)
        assert False, "Result does not match expected output."
    print("Graph 1 test passed.")

    # Test graph 2
    graph2 = [
        [0, 5, inf, 10],
        [inf, 0, 3, inf],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0]
    ]

    expected_result2 = [
        [0, 5, 8, 9],
        [inf, 0, 3, 4],
        [inf, inf, 0, 1],
        [inf, inf, inf, 0]
    ]

    result2 = floyd_warshall(graph2)
    if result2 != expected_result2:
        print("Test failed for graph2!")
        print("Expected:")
        for row in expected_result2:
            print(row)
        print("Got:")
        for row in result2:
            print(row)
        assert False, "Result does not match expected output."
    print("Graph 2 test passed.")

if __name__ == "__main__":
    test_floyd_warshall()
