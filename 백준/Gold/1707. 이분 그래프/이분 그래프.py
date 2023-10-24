import sys

sys.setrecursionlimit(10**6)


def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]:
            return False
    return True


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    bipatite = True
    for i in range(1, V + 1):
        if not visited[i]:
            bipatite = dfs(i, 1)
            if not bipatite:
                break
    print("YES" if bipatite else "NO")
