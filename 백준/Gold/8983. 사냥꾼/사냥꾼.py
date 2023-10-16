import sys


def binarySearch(arrM, lower, upper) -> int:
    global cnt
    start = 0
    end = len(arrM) - 1
    while True:
        if start > end:
            break
        mid = (start + end) // 2  # 중앙
        if lower <= arrM[mid] <= upper:
            cnt += 1
            break
        elif arrM[mid] > upper:
            end = mid - 1
        else:  # arrN[mid]  > find:
            start = mid + 1


# 입력
M, N, L = map(int, sys.stdin.readline().split())  # 사대의 수, 동물의 수, 사정거리
arrM = sorted(list(map(int, sys.stdin.readline().split())))  # 사대의 X좌표
arrN = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 사대의 X좌표
cnt = 0
for x, y in arrN:
    if y > L:
        continue
    binarySearch(arrM, x + y - L, x - y + L)
print(cnt)
