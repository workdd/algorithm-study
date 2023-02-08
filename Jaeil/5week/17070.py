import sys

N = int(sys.stdin.readline().strip())

house = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[[0, 0, 0] for col in range(N)] for row in range(N)]

dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if house[i][j] == 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            if i > 0:
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        if i > 0 and house[i][j] == 0 and house[i][j-1] == 0 and house[i-1][j] == 0:
            dp[i][j][2] += dp[i-1][j-1][2] + dp[i-1][j-1][0] + dp[i-1][j-1][1]

print(sum(dp[N-1][N-1]))