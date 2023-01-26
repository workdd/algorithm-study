import sys

N = int(sys.stdin.readline())

# 세로, 대각, 가로 순서
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

board = []

for i in range(N):
    ipt = list(map(int, sys.stdin.readline().split()))
    board.append(ipt)

dp[0][1][2] = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            if i > 0:
                dp[i][j][0] += dp[i - 1][j][0] + dp[i - 1][j][1]
            if j > 1:
                dp[i][j][2] += dp[i][j - 1][2] + dp[i][j - 1][1]

                if board[i - 1][j] == 0 and board[i][j - 1] == 0:
                    dp[i][j][1] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

ans = 0

for num in dp[N-1][N-1]:
    ans += num

print(ans)