import sys

D, P = map(int, sys.stdin.readline().split())

MAX = 100000

lst = []

for _ in range(P):
    L, C = map(int, sys.stdin.readline().split())

    l = [L, C]
    lst.append(l)

lst.sort()

ans = []


def check(i, d, p):
    if d == D:
        ans.append(p)
        return

    elif d > D:
        return

    for j in range(i + 1, P):
        check(j, d + lst[j][0], min(p, lst[j][1]))

    return


for idx in range(P):
    check(idx, lst[idx][0], lst[idx][1])

print(max(ans))
