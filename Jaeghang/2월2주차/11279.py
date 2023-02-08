import sys
import heapq

N = int(sys.stdin.readline())

max_heap = []

for _ in range(N):
    val = int(sys.stdin.readline())
    if val == 0:
        if len(max_heap) > 0:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -val)
