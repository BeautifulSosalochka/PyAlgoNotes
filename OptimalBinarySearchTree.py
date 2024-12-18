import random

def optimal_bst(keys, freq, n):
    """
    Compute the cost of the Optimal Binary Search Tree (OBST).

    :param keys: A list of keys (sorted in ascending order).
    :param freq: Frequencies of the keys (in the same order as keys).
    :param n: Number of keys.
    :return: Minimum cost of the OBST.
    """
    cost = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + sum(freq[i:j + 1])

                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost

    return cost[0][n - 1]

def generate_large_test_data(size):
    """
    Generate a large test dataset of keys and frequencies.

    :param size: Number of keys.
    :return: Tuple of (keys, frequencies).
    """

    keys = list(range(1, size + 1))
    freq = [random.randint(1, 100) for _ in range(size)]
    return keys, freq

def test_optimal_bst():
    """
    Test the optimal BST algorithm with various datasets.
    """
    print("Testing with small dataset...")
    keys = [10, 20, 30, 40]
    freq = [4, 2, 6, 3]
    n = len(keys)
    print("Keys:", keys)
    print("Frequencies:", freq)
    print("Minimum cost of OBST:", optimal_bst(keys, freq, n))

    print("\nTesting with large dataset...")
    keys, freq = generate_large_test_data(100)
    n = len(keys)
    print("Generated 100 keys and frequencies.")
    print("Minimum cost of OBST:", optimal_bst(keys, freq, n))


if __name__ == "__main__":
    test_optimal_bst()
