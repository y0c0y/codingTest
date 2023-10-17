from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque([])
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    if cmd[0] == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    if cmd[0] == "size":
        print(len(queue))
    if cmd[0] == "empty":
        if not len(queue):
            print(1)
        else:
            print(0)
    if cmd[0] == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    if cmd[0] == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
