import sys
from collections import deque


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
N, M, V = map(int, sys.stdin.readline().split())
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 not in graph:
        graph[v1] = [v2]
    elif v2 not in graph[v1]:
        graph[v1].append(v2)
    if v2 not in graph:
        graph[v2] = [v1]
    elif v1 not in graph[v2]:
        graph[v2].append(v1)

print(DFS(graph, V))
print(BFS(graph, V))
