import sys

result = 0


def binarySearch(find: int) -> int:
    global result
    global arrN
    start = 0
    end = max(arrN)
    while True:
        if start > end:
            return result
        total = 0
        mid = (start + end) // 2  # 중앙
        for h in arrN:
            if h >= mid:
                total += h - mid
        if total >= find:
            result = mid
            start = mid + 1
        else:
            end = mid - 1


# 입력
N, M = map(int, sys.stdin.readline().split())  # 나무의 수 & 나무의 길이
arrN = sorted(list(map(int, sys.stdin.readline().split())))  # 나무들의 높이
print(binarySearch(M))
