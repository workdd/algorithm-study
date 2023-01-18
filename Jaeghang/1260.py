import sys
import copy

N, M, V = map(int, sys.stdin.readline().split())

relations = [[0] * (N + 1) for _ in range(N + 1)]
nodes = [1 for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())

    relations[n1][n2] = 1
    relations[n2][n1] = 1

node = V

dfs_rel = copy.deepcopy(relations)
dfs_stack = [node]

while len(dfs_stack) != 0:
    node = dfs_stack.pop(-1)
    print(node, end=" ")

    lst = dfs_rel[node]

    while node in dfs_stack:
        dfs_stack.remove(node)

    for idx in range(len(lst) - 1, 0, -1):
        if dfs_rel[node][idx] == 1:
            dfs_rel[node][idx] = 0
            dfs_rel[idx][node] = 0
            nodes[node] = 0
            nodes[idx] = 0
            dfs_stack.append(idx)
print()

node = V
nodes = [1 for _ in range(N + 1)]

bfs_rel = copy.deepcopy(relations)

bfs_queue = [node]

while len(bfs_queue) != 0:
    node = bfs_queue.pop(0)
    nodes[node] = 0
    print(node, end=" ")
    lst = bfs_rel[node]

    for idx in range(1, len(lst)):
        if bfs_rel[node][idx] == 1 and nodes[idx] == 1:
            bfs_rel[node][idx] = 0
            bfs_rel[idx][node] = 0
            nodes[node] = 0
            nodes[idx] = 0
            bfs_queue.append(idx)
