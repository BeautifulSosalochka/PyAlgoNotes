import random
import time


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def test_linear_search():
    array_size = int(input("Введите размер массива: "))

    test_array = [random.randint(0, 10_000_000) for _ in range(array_size)]

    target = int(input("Введите число для поиска: "))

    start_time = time.time()
    result = linear_search(test_array, target)
    search_time = time.time() - start_time

    if result != -1:
        print(f"Число найдено, индекс: {result}")
    else:
        print("Число не найдено.")

    print(f"Время выполнения поиска: {search_time:.4f} секунд")


if __name__ == "__main__":
    test_linear_search()
