from collections import deque

n = int(input())

# 각 노드 별로 연결된 노드를 저장하는 집합
graph = [set() for _ in range(n+1)]

# 각 노드의 부모 노드를 저장하는 리스트
parent = [0] * (n+1)

# 입력 받기
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# BFS 탐색 시작
queue = deque([1])

while queue:
    current = queue.popleft()
    for next_node in list(graph[current]):  # 현재 노드와 연결된 노드를 리스트로 변환
        if not parent[next_node]:  # 방문하지 않은 노드만 처리
            parent[next_node] = current
            queue.append(next_node)
            graph[next_node].remove(current)  # 연결 정보 삭제

# 2번 노드부터 부모 노드 출력
for i in range(2, n+1):
    print(parent[i])
