import sys


# 유니온-파인 알고리즘을 위한 부모 노드를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 요소를 합치는 함수
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 초기화: 각 노드는 자신을 부모로 가리킨다.
parent = [i for i in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    union(parent, v1, v2) #노드 부모 연결하기

# 각 노드의 최종 부모 노드를 찾는다.
cnt = -1
for i in range(1, n + 1):
    if find(parent, i) == 1: #부모가 1인 노드 찾기
        cnt += 1

print(cnt) #자기자신 제외
