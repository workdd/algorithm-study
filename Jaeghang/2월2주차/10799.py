import sys

ipt = sys.stdin.readline()

stack = []

ans = 0

for idx in range(len(ipt)):
    st = ipt[idx]

    if st == ')':
        _, s_idx, s_laser = stack.pop()

        if len(stack) > 0:
            stack[-1][2] += s_laser
        if idx - s_idx == 1:
            if len(stack) > 0:
                stack[-1][2] += 1
        else:
            ans += s_laser + 1

    else:
        stack.append(['(', idx, 0])
print(ans)
