import sys

N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())

    board[x - 1][y - 1] = 1

L = int(sys.stdin.readline())

new_directions = []

for _ in range(L):
    X, C = map(str, sys.stdin.readline().split())

    new_directions.append((X, C))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x = y = 0
snakes = [(x, y)]
idx = 0
times = 0

while True:
    times += 1
    current = directions[idx]
    nx = x + current[0]
    ny = y + current[1]

    x = nx
    y = ny

    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        break


    elif (nx, ny) in snakes:
        break

    else:
        if len(new_directions) > 0:
            if times == int(new_directions[0][0]):

                _, direction = new_directions.pop(0)

                if direction == "D":
                    idx += 1
                    idx += 4
                    idx %= 4
                elif direction == "L":
                    idx -= 1
                    idx += 4
                    idx %= 4

        snakes.append((nx, ny))

        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            snakes.pop(0)
print(times)
