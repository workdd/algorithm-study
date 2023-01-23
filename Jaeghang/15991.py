import sys

T = int(sys.stdin.readline())

MAX = 100001
dp = [-1 for _ in range(MAX)]

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
for _ in range(T):
    n = int(sys.stdin.readline())
    if dp[n] != -1:
        print(dp[n] % 1000000009)
    else:
        for idx in range(6, n + 1):
            if dp[idx] == -1:
                dp[idx] = dp[idx - 2] + dp[idx - 4] + dp[idx - 6]
                dp[idx] %= 1000000009
        print(dp[n] % 1000000009)
