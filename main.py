from __future__ import annotations
import sys
import argparse
from time import perf_counter
from typing import List, Tuple, Iterable, Union

Number = Union[int, float]


def read_numbers_from_file(path: str) -> List[Number]:
    """
    공백/줄바꿈/쉼표로 구분된 숫자를 읽어 리스트로 반환.
    가능한 정수(int)로, 아니면 실수(float)로 파싱.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise SystemExit(f"[에러] 파일을 찾을 수 없습니다: {path}")

    tokens = text.replace(",", " ").split()
    nums: List[Number] = []
    for i, t in enumerate(tokens, 1):
        s = t.strip().lower()
        if s in {"+inf", "inf", "-inf", "nan"}:
            raise SystemExit(f"[에러] {i}번째 토큰이 비정상 숫자입니다: {t!r}")
        try:
            if "." in s or "e" in s:
                nums.append(float(s))
            else:
                nums.append(int(s))
        except ValueError:
            raise SystemExit(f"[에러] {i}번째 토큰이 숫자가 아닙니다: {t!r}")
    return nums

def heapify(arr: List[Number], n: int, i: int) -> None:
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



def quick_sort(arr: List[Number], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr: List[Number], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_main(filename):
    numbers = read_numbers_from_file(filename)
    start = perf_counter()
    quick_sort(numbers, 0, len(numbers) - 1)
    elapsed = perf_counter() - start

    print(" ".join(str(x) for x in numbers))
    print(f"\n정렬 소요 시간: {elapsed * 1000:.3f} ms")


   
def bubble_sort(arr: List[Number]) -> None:
    """In-place bubble sort (오름차순)."""
    n = len(arr)
    # 조기 종료 최적화
    for i in range(n - 1):
        swapped = False
        # 마지막 i개는 이미 정렬됨
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



def bubble_main(filename):
    numbers = read_numbers_from_file(filename)

    start = perf_counter()
    bubble_sort(numbers)  # in-place 정렬
    elapsed = perf_counter() - start

    # 정렬 결과 출력 (공백 구분)
    # 정수/실수 섞여 있을 수 있으니 원형 유지하여 그대로 출력
    print(" ".join(str(x) for x in numbers))

    # 소요 시간 출력 (ms)
    print(f"\n정렬 소요 시간: {elapsed * 1000:.3f} ms")


def selection_sort(arr: List[Number]) -> None:
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

def load_ints(path):
    nums = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            for tok in line.split():
                try:
                    nums.append(int(tok))
                except ValueError:
                    pass
    return nums


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


def heap_sort(arr: List[Number]) -> None:
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def insertion_sort(arr: List[Number]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def run_sort(algorithm: str, data: List[Number], reverse: bool) -> Tuple[List[Number], float]:
    """
    선택한 알고리즘으로 정렬 실행.
    in-place 계열은 복사본 만들어서 안전하게 수행.
    merge_sort만 새 리스트 반환.
    """
    if algorithm == "merge":
        start = perf_counter()
        out = merge_sort(data)
        if reverse:
            out.reverse()
        elapsed = perf_counter() - start
        return out, elapsed

    # in-place 알고리즘들
    arr = data[:]  # 원본 보호
    start = perf_counter()
    if algorithm == "quick":
        if arr:
            quick_sort(arr, 0, len(arr) - 1)
    elif algorithm == "heap":
        heap_sort(arr)
    elif algorithm == "bubble":
        bubble_sort(arr)
    elif algorithm == "selection":
        selection_sort(arr)
    elif algorithm == "insertion":
        insertion_sort(arr)
    else:
        raise SystemExit(f"[에러] 지원하지 않는 알고리즘: {algorithm}")
    if reverse:
        arr.reverse()
    elapsed = perf_counter() - start
    return arr, elapsed


def is_sorted(a: Iterable[Number], reverse: bool = False) -> bool:
    it = iter(a)
    try:
        prev = next(it)
    except StopIteration:
        return True
    comp = (lambda x, y: x >= y) if reverse else (lambda x, y: x <= y)
    for cur in it:
        if not comp(prev, cur):
            return False
        prev = cur
    return True


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description="여러 정렬 알고리즘(merge/quick/heap/bubble/selection/insertion) CLI"
    )
    parser.add_argument("algorithm",
                        choices=["merge", "quick", "heap", "bubble", "selection", "insertion"],
                        help="사용할 정렬 알고리즘")
    parser.add_argument("filename", help="입력 데이터 파일 경로")
    parser.add_argument("--reverse", action="store_true", help="내림차순 정렬")
    parser.add_argument("--show-original", action="store_true", help="원본 데이터도 출력")
    parser.add_argument("--no-output", action="store_true", help="정렬 결과를 출력하지 않음(성능 측정용)")
    args = parser.parse_args(argv)

    numbers = read_numbers_from_file(args.filename)
    if args.show_original:
        print("원본 데이터:")
        print(" ".join(str(x) for x in numbers))

    sorted_numbers, elapsed = run_sort(args.algorithm, numbers, args.reverse)

    # 정렬 검증
    if not is_sorted(sorted_numbers, reverse=args.reverse):
        print("[경고] 정렬 검증 실패!", file=sys.stderr)

    if not args.no_output:
        print("정렬 결과:")
        print(" ".join(str(x) for x in sorted_numbers))
    print(f"\n정렬 소요 시간: {elapsed * 1000:.3f} ms")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))