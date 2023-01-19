n, m, v = map(int, input().split())

line_info = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    line_info[a][b] = line_info[b][a] = 1

bfs_visit = [0] * (n + 1)
dfs_visit = [0] * (n + 1)


def bfs(v):
    q = []
    q.append(v)
    bfs_visit[v] = 1

    while len(q) > 0:
        v = q.pop(0)
        print(v, end=' ')

        for i in range(1, n + 1):
            if bfs_visit[i] == 0 and line_info[v][i] == 1:
                q.append(i)
                bfs_visit[i] = 1

def dfs(v):
    dfs_visit[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if dfs_visit[i] == 0 and line_info[v][i] == 1:
            dfs(i)

dfs(v)
print()
bfs(v)
