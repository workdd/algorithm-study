
push_count = 0

def push_left(target):
    global push_count
    while num_list[0] != target:
        temp = num_list[0]
        for i in range(len(num_list)-1):
            num_list[i] = num_list[i+1]

        num_list[len(num_list)-1] = temp
        push_count += 1
    num_list.pop(0)

def push_right(traget):
    global  push_count
    while num_list[0] != traget:
        temp = num_list[len(num_list)-1]
        for i in range(len(num_list)-1, 0, -1):
            num_list[i] = num_list[i-1]

        num_list[0] = temp
        push_count += 1

    num_list.pop(0)


N, M = map(int, input().split())
pop_list = list(map(int, input().split()))
num_list = []
for i in range(N):
    num_list.append(i+1)

for i in pop_list:
    if num_list.index(i) < len(num_list) - num_list.index(i):
        push_left(i)
    else:
        push_right(i)



print(push_count)
