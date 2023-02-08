import sys

N, L, R = map(int, sys.stdin.readline().split())
A = [0 for r in range(N)]

def move(A, visitied, N, L, R, r, c):
    queue = [(r, c)]
    changed = [(r, c)]
    ave = num = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited[r][c] = -1
    while len(queue) > 0:
        now = queue.pop(0)
        ave += A[now[0]][now[1]]
        num += 1
        for nextD in d:
            nextR = now[0] + nextD[0]
            nextC = now[1] + nextD[1]
            if nextR < 0 or N <= nextR or nextC < 0 or N <= nextC or visited[nextR][nextC] != 0 :
                continue
            diff = abs(A[now[0]][now[1]] - A[nextR][nextC])
            if diff < L or R < diff:
                continue
            visited[nextR][nextC] = -1
            queue.append((nextR, nextC))
            changed.append((nextR, nextC))
    ave = ave // num
    for c in changed:
        visited[c[0]][c[1]] = ave

for r in range(N):
    A[r] = list(map(int, sys.stdin.readline().split()))

changed = 0
ans = -1

while changed < N*N:
    changed = 0
    ans += 1
    visited = [[0 for c in range(N)] for r in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                changed += 1
                move(A, visited, N, L, R, r, c)
    A = visited

print(ans)
