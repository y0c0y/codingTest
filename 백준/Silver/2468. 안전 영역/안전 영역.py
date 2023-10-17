import sys
from collections import deque

N = int(sys.stdin.readline())
info = []
visited = []
maxHeights = 0


def setInfo():
    global maxHeights
    for _ in range(N):
        l = list(map(int, sys.stdin.readline().split()))
        if max(l) > maxHeights:
            maxHeights = max(l)
        info.append(l)


def resetVisited() -> None:
    global visited
    # False 로 초기 셋팅
    visited = [[False for _ in range(N)] for _ in range(N)]


def isIndex(y, x):
    if -1 < y < N and -1 < x < N:  # 범위의 인덱스라면
        return True
    else:
        return False


def bfs(y, x, limit):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

    while queue:
        x, y = queue.popleft()
        for dir in direction:
            preY = y + dir[0]
            preX = x + dir[1]
            if isIndex(preY, preX):
                if not visited[preY][preX] and info[preY][preX] > limit:
                    visited[preY][preX] = True
                    queue.append((preX, preY))


setInfo()  # N*N 높이 정보
cnt = 0
totalCnt = 0
answer = 0
for limit in range(maxHeights + 1):
    resetVisited()
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and info[y][x] > limit:
                bfs(y, x, limit)
                cnt += 1
    if cnt > answer:
        answer = cnt
    cnt = 0
print(answer)
