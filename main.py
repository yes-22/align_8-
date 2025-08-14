
import sys

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