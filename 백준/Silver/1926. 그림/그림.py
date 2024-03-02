import sys
from collections import deque

dx = [0, 0, -1, 1]  # 상,하,좌,우
dy = [-1, 1, 0, 0]


def isIndex(y, x):
    global n, m

    if not (0 <= y < n):
        return False
    if not (0 <= x < m):
        return False
    return True


def bfs(y, x):
    global visited, paints

    q = deque()
    q.append((y, x))
    visited[y][x] = True
    size = 1

    while q:
        tmpY, tmpX = q.popleft()
        for i in range(4):
            Y = tmpY + dy[i]
            X = tmpX + dx[i]
            if isIndex(Y, X) and visited[Y][X] == False:
                if paints[Y][X] == 1:
                    q.append((Y, X))
                    visited[Y][X] = True
                    size += 1
    return size


n, m = map(int, sys.stdin.readline().split(" "))

paints = []

visited = [[False] * m for _ in range(n)]

cnt = 0
pM = 0

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    paints.append(tmp)

for y in range(n):
    for x in range(m):
        if paints[y][x] == 1 and visited[y][x] == False:
            tmp = bfs(y, x)
            cnt += 1
            if tmp > pM:
                pM = tmp


print(cnt)
print(pM)
