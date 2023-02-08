import sys

T = int(sys.stdin.readline().strip())
dp = [0] * 100001
dp[0] = dp[1] = dp[2] = dp[3] = 1

for i in range(2, 100001):
    for plus in [2, 4, 6]:
        if i-plus < 0:
            break
        dp[i] = (dp[i] + dp[i-plus]) % 1000000009

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n])
