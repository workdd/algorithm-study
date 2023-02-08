import sys

N = int(sys.stdin.readline())

board = []

for _ in range(N):
    ipt = list(map(str, sys.stdin.readline().split()))
    board += ipt

visited = [[0] * N for _ in range(N)]
directions = [[-1, 0],
              [0, -1],
              [1, 0],
              [0, 1]]


def bfs(sx, sy):
    queue = [(sx, sy)]
    cnt = 1
    visited[sx][sy] = 1

    while len(queue) > 0:
        x, y = queue.pop(0)
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            elif visited[nx][ny] == 0 and board[nx][ny] == '1':
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt


ans = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()

print(len(ans))
for a in ans:
    print(a)
