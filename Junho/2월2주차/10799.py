import sys
input = sys.stdin.readline

parentheses = str(input())

stack = []
cnt = 0
lastPush = ''

for i in range(len(parentheses) - 1):
    parenthesis = parentheses[i]
    stack.append(parenthesis)

    if stack[-1] == ')':
        stack.pop()
        if lastPush == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

    lastPush = parenthesis

print(cnt)