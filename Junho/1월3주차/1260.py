def stackDFS(V):
    stack = [V]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            nextNodes = list(graph[node]).copy()
            nextNodes.sort()
            nextNodes.reverse()
            for nextNode in nextNodes:
                stack.append(nextNode)

    print(' '.join(str(e) for e in visited))
    return

    
def queueBFS(V):
    queue = [V]
    visited = [V]
    
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')

        nextNodes = list(graph[V]).copy()
        nextNodes.sort()
        for node in nextNodes:
            if not node in visited:
                queue.append(node)
                visited.append(node)

# 정점의 개수 N, 간선의 개수 M, 탐색 시작 정점 V
N, M, V = map(int, input().split())

graph = {}

for _ in range(M):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph.keys():
        graph[y] = [x]
    else:
        graph[y].append(x)

stackDFS(V)
queueBFS(V)
print()