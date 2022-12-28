n = int(input())

prev = 1
now = 1
for i in range(2, n):
    tmp = now
    now = prev + now
    prev = tmp

print(now)

