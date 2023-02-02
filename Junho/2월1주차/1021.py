import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
positions = map(int, input().split())
minimum = 0

circle = deque([N for N in range(1, N + 1)])

for value in positions:
  index = circle.index(value)

  rotationR = N - index
  rotationL = index

  if(rotationL <= rotationR):
    minimum += rotationL
    circle.rotate(-rotationL)
  else:
    minimum += rotationR
    circle.rotate(rotationR)
  
  N -= 1
  circle.popleft()

print(minimum)