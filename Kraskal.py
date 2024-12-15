
"""
Output:
---------

Testing Kruskal's algorithm...
Testing Kruskal's algorithm with Union-Find...
Union-Find Kruskal's: Total cost = 13082, Time = 0.01 seconds
Testing Kruskal's algorithm without Union-Find...
Non-Union-Find Kruskal's: Total cost = 13082, Time = 0.02 seconds
"""

from collections import defaultdict
import time
import random

def generate_large_graph(num_nodes, num_edges):
    graph = defaultdict(dict)
    edges = []
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            weight = random.randint(1, 100)
            graph[u][v] = weight
            graph[v][u] = weight
            edges.append((weight, u, v))
    return graph, edges

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_with_union_find(edges, num_nodes):
    uf = UnionFind(num_nodes)
    mst = []
    total_cost = 0

    edges.sort()  # Sort edges by weight

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

def kruskal_without_union_find(edges, num_nodes):
    mst = []
    total_cost = 0
    edges.sort()  # Sort edges by weight

    connected_components = {i: {i} for i in range(num_nodes)}

    for weight, u, v in edges:
        if connected_components[u] is not connected_components[v]:
            mst.append((u, v, weight))
            total_cost += weight

            # Merge components
            new_component = connected_components[u].union(connected_components[v])
            for node in new_component:
                connected_components[node] = new_component

    return mst, total_cost

def test_kruskal():
    num_nodes = 1000
    num_edges = 5000
    _, edges = generate_large_graph(num_nodes, num_edges)

    print("Testing Kruskal's algorithm with Union-Find...")
    start_time = time.time()
    mst_uf, cost_uf = kruskal_with_union_find(edges, num_nodes)
    end_time = time.time()
    print(f"Union-Find Kruskal's: Total cost = {cost_uf}, Time = {end_time - start_time:.2f} seconds")

    print("Testing Kruskal's algorithm without Union-Find...")
    start_time = time.time()
    mst_no_uf, cost_no_uf = kruskal_without_union_find(edges, num_nodes)
    end_time = time.time()
    print(f"Non-Union-Find Kruskal's: Total cost = {cost_no_uf}, Time = {end_time - start_time:.2f} seconds")

def main():
    print("---------")
    print("\nTesting Kruskal's algorithm...")
    test_kruskal()


if __name__ == "__main__":
    main()