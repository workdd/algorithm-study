import sys
import decimal

N = int(sys.stdin.readline())

denote = sys.stdin.readline()
operator = ['*', '+', '/', '-']

stack = []
numbers = []

for _ in range(N):
    N = sys.stdin.readline().strip()
    numbers.append(N)

for d in denote:
    if d in operator:
        n2 = stack.pop()
        n1 = stack.pop()

        if isinstance(n2, str):
            idx2 = ord(n2) - 65
            num2 = numbers[idx2]
        else:
            num2 = str(n2)
        if isinstance(n1, str):
            idx1 = ord(n1) - 65
            num1 = numbers[idx1]
        else:
            num1 = str(n1)
        num = eval(num1 + d + num2)
        stack.append(num)
    else:
        stack.append(d)

ans = round(stack[0], 2)
ans = decimal.Decimal(ans)
print(f"{ans:.2f}")