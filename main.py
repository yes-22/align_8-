
def heapify(arr, n, i):
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


   
def bubble_sort(arr: List[float]) -> List[float]:
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

def read_numbers_from_file(path: str) -> List[float]:
    """공백/줄바꿈으로 구분된 숫자들 읽기 (정수/실수 모두 허용)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise SystemExit(f"[에러] 파일을 찾을 수 없습니다: {path}")

    tokens = text.split()
    numbers: List[float] = []
    for idx, t in enumerate(tokens, 1):
        try:
            # 가능하면 정수로, 아니면 실수로
            if t.strip().lower() in {"+inf", "inf", "-inf", "nan"}:
                raise ValueError("비정상 숫자 토큰")
            if "." in t or "e" in t.lower():
                numbers.append(float(t))
            else:
                numbers.append(int(t))
        except ValueError:
            raise SystemExit(f"[에러] {idx}번째 토큰이 숫자가 아닙니다: {t!r}")
    return numbers

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

if __name__ == '__main__':
   filename = sys.argv[1]
   
   data = load_ints(filename)
   bubble_main(filename) # 버블 정렬 - 강현우
   selection_sort(data)          
   print(*data)   

def selection_sort(arr):
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
        return arr

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("사용법: python main.py <파일명>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        # 파일에서 데이터 읽기
        with open(filename, 'r') as file:
            data = file.read().strip().split()
            # 문자열을 정수로 변환
            numbers = [int(x) for x in data]
        
        print("원본 데이터:", numbers)
        
        # 병합 정렬 수행
        sorted_numbers = merge_sort(numbers)
        
        print("정렬된 데이터:", sorted_numbers)
        
    except FileNotFoundError:
        print(f"파일 '{filename}'을 찾을 수 없습니다.")
    except ValueError:
        print("파일에 유효하지 않은 숫자가 포함되어 있습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

