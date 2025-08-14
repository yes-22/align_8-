
import sys

if __name__ == '__main__':
   filename = sys.argv[1]
   data = load_ints(filename)
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