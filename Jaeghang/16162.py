import sys

N, A, D = map(int, sys.stdin.readline().split())

lst = map(int, sys.stdin.readline().split())

cnt = 0
for n in lst:
    if n == A:
        cnt += 1
        A += D

print(cnt)