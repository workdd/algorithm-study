import sys
import heapq

N = int(sys.stdin.readline())
q = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not len(q):
            print(0)
        else:
            print(abs(heapq.heappop(q)))
    else:
        heapq.heappush(q, -x)
