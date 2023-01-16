import sys

N, M, V = map(int, sys.stdin.readline().strip().split())
Graph = [[0 for col in range(N+1)] for row in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    Graph[x][y] = Graph[y][x] = 1

def DFS(Graph, v, visited):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, len(Graph)):
        if Graph[v][i] == 1 and visited[i] == 0:
            DFS(Graph, i, visited)

def BFS(Graph, v):
    queue = [v]
    visited = [0 for _ in range(len(Graph)+1)]
    visited[v] = 1
    while len(queue)>0:
        nowV = queue.pop(0)
        print(nowV, end=' ')
        for i in range(1, len(Graph)):
            if Graph[nowV][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    print()

DFS(Graph, V, [0 for _ in range(len(Graph)+1)])
print()
BFS(Graph, V)