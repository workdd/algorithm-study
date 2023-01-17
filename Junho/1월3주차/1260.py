def stackDFS():
    stack = []
    stack.append(V)

    while len(stack) != len(graph.keys()):
        nodes = list(graph[stack[-1]])
        for node in nodes:
            if not node in stack:
                stack.append(node)
                break
    
    print(' '.join(str(e) for e in stack))

def recursiveDFS(value):
    print(value, end = ' ')

    nodes = graph.get(value)
    for node in nodes:
        if visit[node] == 0:
            visit[node] = 1
            recursiveDFS(node)
            break
    
def queueBFS():
    print()
# 정점의 개수 N, 간선의 개수 M, 탐색 시작 정점 V
N, M, V = map(int, input().split())
# recursiveDFS 노드 방문 확인 리스트
visit = [0] * (N + 1)
visit[V] = 1

# 인접 리스트(Linked List)
graph = {}

# _는 값 무시의 의미
for _ in range(M):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = set([y])
    else:
        graph[x].add(y)
    if y not in graph.keys():
        graph[y] = set([x])
    else:
        graph[y].add(x)

print(graph)

stackDFS()
recursiveDFS(V)
print()