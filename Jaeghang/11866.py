import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

deq = deque([n for n in range(1, N + 1)])

deq.rotate(-K + 1)

print('<', end="")
while len(deq) > 0:
    num = deq.popleft()
    if len(deq) == 0:
        print(num, end="")
        break
    print(num, end=", ")
    deq.rotate(-K + 1)

print('>')
