import sys
import bisect

N = int(sys.stdin.readline())

index = []

mosquitos = []

for i in range(N):
    TE, TX = map(int, sys.stdin.readline().split())
    mosquitos.append((TE, TX))
    index.append(TE)
    index.append(TX)

index = list(set(index))
index.sort()

idxLen = len(index)
cnt = {}
ans = 0
maxE, maxX = 0, 0

for tE, tX in mosquitos:
    plus = bisect.bisect_left(index, tE)
    minus = bisect.bisect_left(index, tX)
    cnt[plus] = cnt.get(plus, 0) + 1
    cnt[minus] = cnt.get(minus, 0) - 1

for idx in range(idxLen):
    if idx > 0:
        cnt[idx] += cnt[idx-1]
    if cnt[idx] > ans:
        ans = cnt[idx]
        maxE = idx
        maxX = idx+1
    elif cnt[idx] == ans and maxX == idx:
        maxX += 1

print(f"{ans}\n{index[maxE]} {index[maxX]}")