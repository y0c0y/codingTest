import sys

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def dfs(x, y, n):
    if not -1 < x < N or not -1 < y < N:
        return
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end="")
        n //= 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        print(")", end="")
    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")


dfs(0, 0, N)
