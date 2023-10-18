import sys

sys.setrecursionlimit(100000)

white = 0
blue = 0

# def cutPaper(arr, n):
#     global white, blue

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def dfs(x, y, n):
    global blue, white
    if not -1 < x < N or not -1 < y < N:
        return
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                check = -1
                break
    if check == -1:
        n //= 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
    elif check == 1:
        blue += 1
    else:
        white += 1


dfs(0, 0, N)

print(white)
print(blue)
