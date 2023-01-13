import sys
N, M, K, T = map(int, sys.stdin.readline().split())

board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

mold = []

spread_lst = [[-1, -2], [-2, -1], [-2, 1], [-1, 2],
              [1, 2], [2, 1], [2, -1], [1, -2]]


def spread(x, y, t):
    if t == T:
        return

    board[x][y] -=1

    for sp in spread_lst:
        nx = x + sp[0]
        ny = y + sp[1]

        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue

        board[nx][ny] += 1
        spread(nx, ny, t + 1)


for m in range(M):
    mx, my = map(int, sys.stdin.readline().split())

    board[mx][my] = 1
    mo = [mx, my]
    mold.append(mo)

for m in mold:
    spread(m[0], m[1], 0)

clean = 0

for k in range(K):
    kx, ky = map(int,sys.stdin.readline().split())

    if board[kx][ky] >= 1:
        clean = 1

if clean == 0 :
    print("NO")

elif clean == 1:
    print("YES")
