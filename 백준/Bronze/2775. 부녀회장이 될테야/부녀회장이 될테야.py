import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  k = int(input()) #층
  n = int(input()) #호실
  f0 = [x for x in range(1, n+1)]  # 0층 리스트
  for k in range(k):
    for i in range(1,n):
      f0[i] += f0[i-1]
  print(f0[-1])