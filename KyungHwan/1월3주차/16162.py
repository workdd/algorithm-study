n, a, d = map(int, input().split())
node_list = list(map(int, input().split()))
count = 0

for i in range(n):
    if node_list[i] == a + (count * d):
        count += 1

print(count)
