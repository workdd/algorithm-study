def stackDFS(V):
    stack = [V]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            if node not in graph.keys():
                break
            
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
        node = queue.pop(0)
        print(node, end = ' ')

        if node not in graph.keys():
            break

        nextNodes = list(graph[node]).copy()
        nextNodes.sort()
        for nextNode in nextNodes:
            if not nextNode in visited:
                queue.append(nextNode)
                visited.append(nextNode)

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