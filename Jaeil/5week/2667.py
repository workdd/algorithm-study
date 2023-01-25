import sys

N = int(sys.stdin.readline().strip())
Map = [[int(char) for char in sys.stdin.readline().strip()] for _ in range(N)]
houses = []

def BFS(x, y):
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(x, y)]
    Map[x][y] = 0
    cnt = 0
    while len(queue)>0:
        cnt += 1
        nowG = queue.pop(0)
        for d in DIR:
            nextG = (nowG[0] + d[0], nowG[1] + d[1])
            if nextG[0] < 0 or N <= nextG[0] or nextG[1] < 0 or N <= nextG[1]:
                continue
            if Map[nextG[0]][nextG[1]] == 0:
                continue
            queue.append(nextG)
            Map[nextG[0]][nextG[1]] = 0
    return cnt

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            houses.append(BFS(i, j))

print(len(houses))
for _ in sorted(houses):
    print(_)