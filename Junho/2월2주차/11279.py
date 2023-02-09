import heapq

import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    X = int(input())

    if X == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -X)