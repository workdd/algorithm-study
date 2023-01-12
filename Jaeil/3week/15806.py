import sys

N, M, K, t = map(int, sys.stdin.readline().strip().split())

Mold = []
Infested = [[0 for a in range(N+1)] for b in range(N+1)]
Check = []

for i in range(M):
    Mx, My = map(int, sys.stdin.readline().strip().split())
    Mold.append((Mx, My))

for i in range(K):
    Kx, Ky = map(int, sys.stdin.readline().strip().split())
    Check.append(((Kx, Ky), 0))

def BFS(N, Mold, Infested, Check, t):
    d = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    while len(Check)>0:
        nowG, nowT = Check[0]
        Check.pop(0)
        if nowT == t:
            if nowG in Mold:
                print("YES")
                return
            continue
        canInfest = False
        for nextDir in d:
            nextX = nowG[0] + nextDir[0]
            nextY = nowG[1] + nextDir[1]
            if nextX < 1 or N < nextX or nextY < 1 or N < nextY:
                continue
            canInfest = True
            if Infested[nextX][nextY] != 0:
                continue
            Check.append(((nextX, nextY), nowT+1))
            Infested[nextX][nextY] = nowT+1
        if canInfest:
            if (t - nowT) % 2 == 0 and nowG in Mold:
                print("YES")
                return
    print("NO")

BFS(N, Mold, Infested, Check, t)
