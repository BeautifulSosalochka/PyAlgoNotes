from functools import lru_cache

def weighted_independent_set(weights):
    """
    Finds the maximum weight of an independent set in a path graph.

    Args:
        weights (list[int]): List of weights for each vertex.

    Returns:
        int: Maximum weight of the independent set.
        list[int]: List of vertices in the maximum independent set.
    """
    n = len(weights)

    if n == 0:
        return 0, []

    @lru_cache(None)
    def max_weight(i):
        if i < 0:
            return 0
        return max(max_weight(i - 1), weights[i] + max_weight(i - 2))

    def reconstruct():
        selected = []
        i = n - 1
        while i >= 0:
            if max_weight(i) == weights[i] + (max_weight(i - 2) if i - 2 >= 0 else 0):
                selected.append(i)
                i -= 2
            else:
                i -= 1
        selected.reverse()
        return selected

    return max_weight(n - 1), reconstruct()


def test_weighted_independent_set():
    test_cases = [
        ([4, 1, 1, 9, 4], (13, [0, 3])),
        ([1, 2, 3, 4, 5], (9, [1, 3])),
        ([10, 1, 1, 10], (20, [0, 3])),
        ([1, 1, 1, 1], (2, [0, 2])),
        ([], (0, [])),
        ([7], (7, [0])),
    ]

    for weights, expected in test_cases:
        result = weighted_independent_set(weights)
        assert result == expected, f"Failed for weights {weights}: got {result}, expected {expected}"

    print("All test cases passed!")

if __name__ == "__main__":
    weights = list(map(int, input("Enter weights separated by space: ").split()))
    max_weight, vertices = weighted_independent_set(weights)
    print(f"Maximum weight: {max_weight}")
    print(f"Selected vertices: {vertices}")
    test_weighted_independent_set()
