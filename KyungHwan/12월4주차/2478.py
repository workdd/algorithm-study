n = int(input())

if n <=1:
    print(1)
else:
    a = 0
    b = 1
    total = 0
    for i in range(2, n+1):
        total = a + b
        a = b
        b = total
    print(total)