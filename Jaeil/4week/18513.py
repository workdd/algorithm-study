import sys

N, K = map(int, sys.stdin.readline().strip().split())

pond = list(map(int, sys.stdin.readline().strip().split()))
visited = {}

for i in range(len(pond)):
    visited[pond[i]] = True
    pond[i] = (pond[i], 0)

unHappy = 0
cntK = 0

while len(pond) > 0:
    nowG, nowH = pond.pop(0)
    for _ in [-1, 1]:
        if nowG + _ not in visited:
            pond.append((nowG+_, nowH+1))
            visited[nowG+_] = True
            unHappy += nowH+1
            cntK+=1
            if cntK == K:
                print(unHappy)
                exit(0)
