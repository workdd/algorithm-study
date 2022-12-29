n, m = map(int, input().split())

p_list = []

def perm():
    if len(p_list) == m:
        for i in p_list:
            print(i, end=' ')
        print()
        return

    for i in range(1, n + 1):
        p_list.append(i)
        perm()
        p_list.pop()

perm()


