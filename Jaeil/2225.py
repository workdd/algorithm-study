N, K = map(int, input().split())

dp = [[0 for col in range(201)] for row in range(201)]

for k in range(K+1):
    dp[0][k] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = (dp[n][k-1] + dp[n-1][k]) % 1000000000

print(dp[N][K])
