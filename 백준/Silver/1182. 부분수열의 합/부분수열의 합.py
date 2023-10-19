import sys
import itertools

N, S = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

particularL = [list(itertools.combinations(L, i)) for i in range(1, N + 1)]
cnt = 0
# print(particularL)
for part in particularL:
    for p in part:
        if S == sum(p):
            cnt += 1
print(cnt)
