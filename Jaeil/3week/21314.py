import sys

NUM = sys.stdin.readline().strip()

MAX = ''
MIN = ''

st = 0
for i in range(len(NUM)):
    if NUM[i] == 'K':
        if st < i:
            MAX += str(5 * (10 ** (i-st)))
            MIN += str(10 ** (i-st-1)) + '5'
        else:
            MAX += '5'
            MIN += '5'
        st = i+1
    elif i+1 == len(NUM):
        MAX += '1' * (i-st+1)
        MIN += str(10 ** (i-st))

print(f'{MAX}\n{MIN}')