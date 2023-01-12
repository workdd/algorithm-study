n,k = map(int,input().split())


#2차원 배열 생성
dp = [[0] * 201 for i in range(201)]

#k가 1이면 무조건 다 1이고 n이 1이면 k와 같은 값이 배열에 들어감
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

#dp[i][j] 값은 그 값의 위치의 왼쪽 위쪽의 값의 합이다.
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[k][n])