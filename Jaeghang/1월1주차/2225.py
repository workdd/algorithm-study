N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

dp[0][1] = 1
dp[1][1] = 2


for i in range(N+1):
    for j in range(1,K+1):
        if i == 0:
            dp[i][j] = 1
            continue
        if j == 1:
            dp[i][j] = 1
            continue
        for k in range(i+1):
            dp[i][j] += dp[k][j-1]


print(dp[N][K] % 1000000000)