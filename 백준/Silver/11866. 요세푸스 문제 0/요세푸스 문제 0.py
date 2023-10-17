from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
queue = deque([(i + 1) for i in range(N)])
idx = K - 1
print(f"<{queue[idx]}", end="")

while True:
    del queue[idx]
    if len(queue):
        idx = (idx + K - 1) % len(queue)
    else:
        break
    print(f", {queue[idx]}", end="")
print(">", end="")
