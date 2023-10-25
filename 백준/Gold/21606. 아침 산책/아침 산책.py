import sys


n = int(sys.stdin.readline())
inNOut = list(map(int, sys.stdin.readline().strip()))


def setVisitedFalse():
    return [False for _ in range(n + 1)]


graph = {}
for i in range(n):
    graph[i + 1] = [[], inNOut[i]]

totalWay = []


def dfs(start, visited):
    visited[start] = True
    for i in graph[start][0]:
        if not visited[i]:
            for j in graph[i][0]:
                # print(f"in dfs {j}")
                if graph[j][1]:
                    # print(visited)
                    totalWay.append(visited)
                    return
                visited[j] = True
                dfs(i, visited)
    return


for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][0].append(v)
    graph[v][0].append(u)

# print(graph)

for i in range(n):
    if inNOut[i]:
        # print(f"i =={i} and {graph[i + 1][0]}")
        for j in graph[i + 1][0]:
            # print(j)
            visited = dfs(j, setVisitedFalse())
            # print(visited)
print(len(totalWay))
