testCase = int(input())

exe_list = [1,7,4,2,6,8,10,18,22]

for _ in range(testCase):
    num = int(input())
    if num < 11:
        print(exe_list[num-2], end=' ')
    else:
        count_8 = num // 7
        then = num % 7
        if then == 1:
            count_8 -= 1
            print('10', end='')
            print('8' * count_8, end=' ')
        elif then == 2:
            print('1', end='')
            print('8' * count_8, end=' ')
        elif then == 3:
            print('200', end='')
            count_8 -= 2
            print('8' * count_8, end=' ')
        elif then == 4:
            count_8 -= 1
            print('20', end='')
            print('8' * count_8, end=' ')
        elif then == 5:
            print('2', end='')
            print('8' * count_8, end=' ')
        elif then == 6:
            print('6', end='')
            print('8' * count_8, end=' ')
        else:
            print('8' * count_8, end=' ')

    if num % 2 == 0:
        count_1 = num // 2
        print('1' * count_1)
    elif num == 2:
        print('1')
    else:
        count_1 = (num-3)// 2
        print('7', end='')
        print('1' * count_1)
