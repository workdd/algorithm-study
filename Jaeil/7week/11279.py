from heapq import heappush, heappop
import sys

N = int(input())

MAX_HEAP = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(MAX_HEAP) == 0:
            print(0)
        else:
            print(-heappop(MAX_HEAP))
    else:
        heappush(MAX_HEAP, -x)
