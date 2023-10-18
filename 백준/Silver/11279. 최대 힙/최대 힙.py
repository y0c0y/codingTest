import sys
import heapq

sys.setrecursionlimit(100000)

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    value = int(sys.stdin.readline())
    if not value:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -value)
