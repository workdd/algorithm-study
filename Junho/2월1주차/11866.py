import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

circle = deque([N for N in range(1, N + 1)])

print('<', end='')

for i in range(N):
  circle.rotate(-K)
  
  if(i != N - 1):
    print(circle.pop(), end=', ')
  else:
    print(circle.pop(), end='')

print('>')