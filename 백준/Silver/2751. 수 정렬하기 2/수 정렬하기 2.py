import sys

answer = []
N = int(input())
for _ in range(N):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in answer:
    print(i)