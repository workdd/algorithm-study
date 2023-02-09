str = input()

count = 0
bar = 0

for idx, val in enumerate(str):
    if val == ")":
        if str[idx - 1] == ")":
            bar -= 1
            count += 1
        else:
            bar -= 1
            count += bar
    else:
        bar += 1

print(count)


