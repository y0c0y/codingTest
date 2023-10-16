import sys


def binarySearch(find: int) -> None:
    global arrN
    start = 0
    end = len(arrN) - 1
    while True:
        mid = (start + end) // 2  # 중앙 인덱스
        if arrN[mid] == find:
            print(1)
            return
        elif arrN[mid] < find:
            start = mid + 1
        else:
            end = mid - 1
        if start > end:
            break
    print(0)


# 입력
N = int(sys.stdin.readline())
arrN = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().split()))

for find in arrM:
    binarySearch(find)
