pipe = input()
nowOn = 0
num = 0

for i in range(len(pipe)):
    if pipe[i] == '(' and pipe[i+1] != ')':
        num += 1
        nowOn += 1
    elif pipe[i] == ')' and pipe[i-1] == '(':
        num += nowOn
    elif pipe[i] == ')':
        nowOn -= 1

print(num)