import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())  # n*n 크기, k개의 바이러스
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dirctionX = [0, 0, 1, -1]
dirceionY = [1, -1, 0, 0]
visited = [[False for _ in range(n)] for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virus.append([board[i][j], (i, j)])
virus.sort()


def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    visited[x][y] = True
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dirctionX[i]
            ny = y + dirceionY[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 0 and not visited[nx][ny]:
                board[nx][ny] = board[x][y]
                refill.append([board[x][y], (nx, ny)])
                # visited[nx][ny] = True
    # print(board)


s, x, y = map(int, sys.stdin.readline().split())
flag = 0
for _ in range(s):
    refill = []
    while virus:
        value, dire = virus.pop(0)
        a, b = dire
        bfs(a, b)
    virus = refill

# print(board)
print(board[x - 1][y - 1])
