import sys
from collections import deque

directions = [
    (0, -1, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]  # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 # (X, Y, Z)

M, N, H = map(int, sys.stdin.readline().split())

boxes = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)
]
day = 0


def isIndex(x, y, z):
    if -1 < x < M and -1 < y < N and -1 < z < H:
        return True
    return False


def resetVisited():
    return [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]


def bfs():
    deq = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if boxes[z][y][x] == 1:
                    deq.append((x, y, z))
    cnt = 0
    while deq:
        for _ in range(len(deq)):
            x, y, z = deq.popleft()
            for nx, ny, nz in directions:
                dx = x + nx
                dy = y + ny
                dz = z + nz
                if isIndex(dx, dy, dz) and not boxes[dz][dy][dx]:
                    boxes[dz][dy][dx] += 1
                    deq.append((dx, dy, dz))
        cnt += 1
    return cnt


day = bfs()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[k][i][j] == 0:
                print(-1)
                exit(0)

print(day - 1)
