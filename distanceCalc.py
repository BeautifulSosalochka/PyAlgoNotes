import math
from typing import Tuple


def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def test_euclidean_distance():
    p1 = (1e9, 2e9)
    p2 = (3e9, 4e9)
    expected = math.sqrt((3e9 - 1e9) ** 2 + (4e9 - 2e9) ** 2)

    assert math.isclose(euclidean_distance(p1, p2), expected), "Failed"
    print("Succeed")


if __name__ == "__main__":
    x1, y1 = map(float, input("Enter coordinates of first point (x1, y1): ").split())
    x2, y2 = map(float, input("Enter the second one (x2, y2): ").split())

    print(f"Euclidean distance: {euclidean_distance((x1, y1), (x2, y2))}")

    test_euclidean_distance()
