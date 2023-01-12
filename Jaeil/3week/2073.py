import sys

D, P = map(int, sys.stdin.readline().strip().split())

PIPES = []
DP = [0 for _ in range(D+1)]

for i in range(P):
    L, C = map(int, sys.stdin.readline().strip().split())
    for j in range(D-L, 0, -1):
        minVal = min(DP[j], C)
        if minVal > DP[j+L]:
            DP[j+L] = minVal
    if DP[L] < C:
        DP[L] = C

print(DP[D])