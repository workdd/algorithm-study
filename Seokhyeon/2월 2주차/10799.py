N = list(input())

stack = []
cnt = 0
for i in range(0, len(N)):
    if N[i] == '(':
        stack.append(N[i])
    else:
        stack.pop()
        if N[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)