import sys

N, K = map(int, sys.stdin.readline().split())

water = list(map(int, sys.stdin.readline().split()))

visited = {}

for i in range(len(water)):
    visited[water[i]] = 1
    water[i] = (water[i], 0)

check = [-1, 1]

cnt = 0
ans = 0
while len(water) > 0:
    position, distance = water.pop(0)
    for c in check:
        if c + position not in visited:
            visited[c + position] = 1
            water.append((c + position, distance + 1))
            cnt += 1
            ans += distance + 1
            if cnt == K:
                print(ans)
                exit(0)
