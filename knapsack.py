import random

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items


def test_knapsack():

    num_items = 1000
    max_value = 100
    max_weight = 50
    capacity = 1000

    values = [random.randint(1, max_value) for _ in range(num_items)]
    weights = [random.randint(1, max_weight) for _ in range(num_items)]

    max_cost, selected_items = knapsack(values, weights, capacity)

    print(f"Максимальная стоимость: {max_cost}")
    print(f"Выбранные предметы: {selected_items[:10]}... (всего {len(selected_items)})")


if __name__ == "__main__":
    test_knapsack()
