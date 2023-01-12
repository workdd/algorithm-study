gyeam = input()

cnt = 0

answer_max = ""
answer_min = ""

for idx in range(len(gyeam)):
    if gyeam[idx] == 'M':
        cnt += 1

    elif gyeam[idx] == 'K':
        max_num = str(5 * (10 ** cnt))

        min_num = str(10 ** (cnt - 1)) + '5'
        if cnt == 0:
            min_num = '5'


        answer_max += max_num
        answer_min += min_num

        cnt = 0

if cnt > 0:
    max_num = '1' * cnt
    min_num = str(10 ** (cnt - 1))

    answer_max += max_num
    answer_min += min_num

print(answer_max)
print(answer_min)