import sys
from collections import deque

n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
dirctionX = [0, 0, 1, -1]
dirceionY = [1, -1, 0, 0]


def bfs(x, y):
    global cnt
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
            if board[nx][ny] == 1 and not visited[nx][ny]:
                deq.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1


ans = [0, []]
cnt = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            ans[0] += 1
            bfs(i, j)
            # print(cnt)
            ans[1].append(cnt)
            cnt = 1

print(ans[0])
for i in sorted(ans[1]):
    print(i)
