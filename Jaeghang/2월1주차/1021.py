import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())

deq_left = deque([n for n in range(1, N + 1)])
deq_right = deque([n for n in range(1, N + 1)])

cnt = 0

num_list = list(map(int, sys.stdin.readline().split()))
for num in num_list:
    loop = len(deq_left)
    for _ in range(loop):
        if num == deq_left[0]:
            deq_left.popleft()
            deq_right = copy.deepcopy(deq_left)
            break
        elif num == deq_right[0]:
            deq_right.popleft()
            deq_left = copy.deepcopy(deq_right)
            break

        else:
            deq_left.rotate(-1)
            deq_right.rotate(1)
            cnt+=1

print(cnt)
