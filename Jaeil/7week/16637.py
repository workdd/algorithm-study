N = int(input())
equation = input()

def calc(equation, val, idx):
    if idx > len(equation):
        return val
    ans = 0
    if idx == 0:
        return max(calc(equation, int(equation[0]), 2), calc(equation, eval(equation[:3]), 4))
    elif idx+2 > len(equation):
        return calc(equation, eval(str(val)+equation[idx-1:idx+1]), idx+2)
    else:
        return max(calc(equation, eval(str(val)+equation[idx-1:idx+1]), idx+2), calc(equation, eval(str(val)+equation[idx-1]+str(eval(equation[idx:idx+3]))), idx+4))

print(calc(equation, 0, 0))