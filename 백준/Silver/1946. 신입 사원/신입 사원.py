import sys

T = int(sys.stdin.readline())  # 테스트 케이스 개수

for _ in range(T):
    n = int(sys.stdin.readline())
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    rank.sort(key=lambda x: x[0])
    cnt = 1
    maxRank = rank[0][1]
    for i in range(n):
        if rank[i][1] < maxRank:
            cnt += 1
            maxRank = rank[i][1]
    print(cnt)
