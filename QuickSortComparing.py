import random
import time

"""
QuickSort Time: 3.8181 seconds
Built-in Sort Time: 0.2300 seconds
Sorting Correctness: Passed
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def test_sorting_algorithms():
    array_size = 1_000_000
    test_array = [random.randint(0, 10_000_000) for _ in range(array_size)]

    start_time = time.time()
    sorted_quicksort = quicksort(test_array.copy())
    quicksort_time = time.time() - start_time

    start_time = time.time()
    sorted_builtin = sorted(test_array.copy())
    builtin_time = time.time() - start_time

    is_correct = sorted_quicksort == sorted_builtin

    return quicksort_time, builtin_time, is_correct


if __name__ == "__main__":
    quicksort_time, builtin_time, is_correct = test_sorting_algorithms()
    print(f"QuickSort Time: {quicksort_time:.4f} seconds")
    print(f"Built-in Sort Time: {builtin_time:.4f} seconds")
    print(f"Sorting Correctness: {'Passed' if is_correct else 'Failed'}")
