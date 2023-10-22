import sys

V, E = map(int, sys.stdin.readline().split())  # 정점, 간선

parent = [i for i in range(V + 1)]  # 부모 테이블 #자기 자신으로 초기화


# 부모찾기 함수
def findParent(x):
    global parent
    if parent[x] != x:  # 부모가 자기 자신이 아니라면
        parent[x] = findParent(parent[x])  # 계속 올라가기 (경로 압축)
    return parent[x]


# union(서로수 - 사이클 확인)
def unionParent(f, t):
    global parent
    f = findParent(f)
    t = findParent(t)
    if f < t:  # 정점 번호가 작은게 우선
        parent[t] = f
    else:
        parent[f] = t


# MST 비용 계산
totalCost = 0
# 최소 신장 트리
MST = []


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]  # 그래프 정보
graph.sort(key=lambda x: x[2])  # (from , to, cost) #코스트를 기준으로 오름차순

for info in graph:
    f, t, cost = info
    if findParent(f) != findParent(t):  # f와 t가 서로 다른 집합에 속해 있으면 (부모가 같지 않다면)
        unionParent(f, t)
        MST.append((f, t))
        totalCost += cost

# print(MST)
print(totalCost)
