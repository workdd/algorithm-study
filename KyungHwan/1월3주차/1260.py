N, M, V = list(map(int, input().split()))
matrix = [[0] * (N + 1) for i in range(N + 1)]


bangmoon = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def dfs(V):
    bangmoon[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if (bangmoon[i] == 0 and matrix[V][i] == 1):
            dfs(i)


def bfs(V):
    q = [V]
    bangmoon[V] = 0
    while q:
        V = q.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if bangmoon[i] == 1 and matrix[V][i] == 1:
                q.append(i)
                bangmoon[i] = 0


dfs(V)
print()
bfs(V)