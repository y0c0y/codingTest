import sys

def dfs(start, now, value, cnt):
    global ans
    if cnt == n:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return
    if value > ans:
        return
    for i in range(n):
        if not visited[i] and a[now][i]:
            visited[i] = True
            dfs(start, i , value+a[now][i], cnt+1)
            visited[i] = False

n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = sys.maxsize
visited = [False]*n
for i in range(n):
    visited[i] = True
    dfs(i,i,0,1)
    visited[i] =False
print(ans)


