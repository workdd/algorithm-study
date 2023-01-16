import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())
    numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    minNums = [-1 for _ in range(n+1)]
    minNums[0] = 0
    minNums[2] = 1
    for i in range(3, n+1):
        for j in range(len(numbers)):
            if i - numbers[j] < 0 or minNums[i - numbers[j]] == -1:
                continue
            newNum = minNums[i - numbers[j]] * 10 + j
            if newNum == 0:
                continue
            if minNums[i] == -1 or minNums[i] > newNum:
                minNums[i] = newNum
    print(minNums[n], end=' ')

    if n%2 == 1:
        print("7" + "1" * ((n-3)//2))
    else:
        print("1" * (n//2))
