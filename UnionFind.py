
"""
Output:
Performing union operations...
Performing find operations...
Union-Find test passed!

"""

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

def test_union_find():
    size = 100000
    uf = UnionFind(size)

    print("Performing union operations...")
    for i in range(0, size - 1, 2):
        uf.union(i, i + 1)

    print("Performing find operations...")
    for i in range(0, size, 2):
        assert uf.find(i) == uf.find(i + 1), "Find operation failed!"

    print("Union-Find test passed!")

def main():
    test_union_find()

if __name__ == "__main__":
    main()