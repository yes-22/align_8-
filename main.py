import sys
from time import perf_counter
from typing import List

def quick_sort(arr: List[float], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr: List[float], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def read_numbers_from_file(path: str) -> List[float]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    tokens = text.replace(",", " ").split()
    return [float(t) if "." in t or "e" in t.lower() else int(t) for t in tokens]

def quick_main(filename):
    numbers = read_numbers_from_file(filename)
    start = perf_counter()
    quick_sort(numbers, 0, len(numbers) - 1)
    elapsed = perf_counter() - start

    print(" ".join(str(x) for x in numbers))
    print(f"\n정렬 소요 시간: {elapsed * 1000:.3f} ms")

if __name__ == '__main__':
    filename = sys.argv[1]
    quick_main(filename)
