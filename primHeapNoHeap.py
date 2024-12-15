
"""
Result:
Testing Prim's algorithm with heap...
Heap-based Prim's: Total cost = 12659, Time = 0.01 seconds
Testing Prim's algorithm without heap...
Non-heap Prim's: Total cost = 12659, Time = 0.31 seconds
"""

import heapq
from collections import defaultdict
import time
import random

def prim_with_heap(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, current_node, previous_node)
    total_cost = 0

    while min_heap:
        cost, current, previous = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if previous is not None:
            mst.append((previous, current, cost))
            total_cost += cost

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, current))

    return mst, total_cost

def prim_without_heap(graph, start):
    mst = []
    visited = set()
    total_cost = 0
    edges = [(0, start, None)]  # (cost, current_node, previous_node)

    while edges:
        edges.sort()  # Sort edges manually
        cost, current, previous = edges.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if previous is not None:
            mst.append((previous, current, cost))
            total_cost += cost

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                edges.append((weight, neighbor, current))

    return mst, total_cost

def generate_large_graph(num_nodes, num_edges):
    graph = defaultdict(dict)
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            weight = random.randint(1, 100)
            graph[u][v] = weight
            graph[v][u] = weight
    return graph

def test_prim():
    num_nodes = 1000
    num_edges = 5000
    graph = generate_large_graph(num_nodes, num_edges)
    start_node = 0

    print("Testing Prim's algorithm with heap...")
    start_time = time.time()
    mst_heap, cost_heap = prim_with_heap(graph, start_node)
    end_time = time.time()
    print(f"Heap-based Prim's: Total cost = {cost_heap}, Time = {end_time - start_time:.2f} seconds")

    print("Testing Prim's algorithm without heap...")
    start_time = time.time()
    mst_no_heap, cost_no_heap = prim_without_heap(graph, start_node)
    end_time = time.time()
    print(f"Non-heap Prim's: Total cost = {cost_no_heap}, Time = {end_time - start_time:.2f} seconds")

def main():
    test_prim()

if __name__ == "__main__":
    main()