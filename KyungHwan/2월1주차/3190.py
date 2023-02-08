dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = 0
y = 0
current_direction = 0
N = int(input())
K = int(input())

matrix = [[0 for _ in range(N)] for _ in range(N)]

apple_xy = []
for _ in range(K):
    apple_x, apple_y = map(int, input().split())
    matrix[apple_x-1][apple_y-1] = 1

L = int(input())
direction_list = []

for _ in range(L):
    X, C = map(str, input().split())
    direction_list.append((int(X), C))


second = 0
change_direction_second = direction_list[0][0]
snake_body = [(0,0)]

while True:
    second += 1
    x += dx[current_direction]
    y += dy[current_direction]
    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if (x,y) in snake_body:
        break

    if second == change_direction_second:
        if 'L' == direction_list[0][1]:
            current_direction = (current_direction - 1) % 4
        else:
            current_direction = (current_direction + 1) % 4
        direction_list.pop(0)
        if direction_list:
            change_direction_second = direction_list[0][0]


    if matrix[x][y] == 1:
        matrix[x][y] = 0
        snake_body.append((x,y))
    elif matrix[x][y] == 0:
        snake_body.append((x,y))
        snake_body.pop(0)
    else:
        break


print(second)

