N = int(input())
prev = 2
for i in range(N):
    if i==N-1 and prev==2:
        print(3)
    elif prev == 1:
        prev = 2
        print(2, end=' ')
    else:
        prev = 1
        print(1, end=' ')
