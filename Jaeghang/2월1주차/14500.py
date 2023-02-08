import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for n in range(N):
    ipt = list(map(int, sys.stdin.readline().split()))
    board.append(ipt)

max_val = max(map(max, board))
check = [[0 for _ in range(M)] for _ in range(N)]

ans = 0

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def dfs(x, y, sum_val, length):
    global ans

    if sum_val + max_val * (4 - length) <= ans:
        return
    if length == 4:
        ans = max(sum_val, ans)
        return

    for k in range(4):
        nx = x + direction[k][0]
        ny = y + direction[k][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if check[nx][ny] == 0:
            if length == 2:
                check[nx][ny] = 1
                dfs(x, y, sum_val + board[nx][ny], length + 1)
                check[nx][ny] = 0

            check[nx][ny] = 1
            dfs(nx, ny, sum_val + board[nx][ny], length + 1)
            check[nx][ny] = 0


for i in range(N):
    for j in range(M):
        check[i][j] = 1
        dfs(i, j, board[i][j], 1)
        check[i][j] = 0

print(ans)
