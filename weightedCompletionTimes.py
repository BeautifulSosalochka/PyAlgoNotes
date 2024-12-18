from typing import List, Tuple

def minimize_weighted_completion_times_difference(jobs: List[Tuple[int, int]]) -> int:
    """
    Minimize the sum of weighted completion times using the greedy difference rule (weight - length).

    :param jobs: List of jobs, each represented as a tuple (weight, length)
    :return: The minimized weighted completion time
    """
    jobs.sort(key=lambda job: (job[0] - job[1], job[0]), reverse=True)

    completion_time = 0
    total_weighted_completion_time = 0

    for weight, length in jobs:
        completion_time += length
        total_weighted_completion_time += weight * completion_time

    return total_weighted_completion_time


def minimize_weighted_completion_times_ratio(jobs: List[Tuple[int, int]]) -> int:
    """
    Minimize the sum of weighted completion times using the greedy ratio rule (weight / length).

    :param jobs: List of jobs, each represented as a tuple (weight, length)
    :return: The minimized weighted completion time
    """
    jobs.sort(key=lambda job: job[0] / job[1], reverse=True)

    completion_time = 0
    total_weighted_completion_time = 0

    for weight, length in jobs:
        completion_time += length
        total_weighted_completion_time += weight * completion_time

    return total_weighted_completion_time


def test_minimization_algorithms():
    """
    Test the greedy algorithms for minimizing weighted completion times.
    """
    jobs = [
        (3, 5),  # weight = 3, length = 5
        (1, 2),
        (4, 3),
        (2, 1)
    ]

    print("Testing Difference Rule...")
    diff_result = minimize_weighted_completion_times_difference(jobs)
    print("Total weighted completion time (difference rule):", diff_result)

    print("\nTesting Ratio Rule...")
    ratio_result = minimize_weighted_completion_times_ratio(jobs)
    print("Total weighted completion time (ratio rule):", ratio_result)


if __name__ == "__main__":
    test_minimization_algorithms()
