n, k = map(int, input().split())
s = []
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.pop(0)
    print(s.pop(0), end='')
    if s:
        print(', ', end='')
print('>')