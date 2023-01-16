import sys

D, P = map(int, sys.stdin.readline().strip().split())

dp = [0 for _ in range(D + 1)]

for _ in range(P):
    L, C = map(int, sys.stdin.readline().strip().split())
    loop = D - L
    for idx in range(loop, 0, -1):
        if dp[idx] == 0:
            continue

        new_val = min(C, dp[idx])
        if dp[idx + L] < new_val:
            dp[idx + L] = new_val

    if dp[L] < C:
        dp[L] = C
print(dp[D])
