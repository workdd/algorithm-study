import sys

N, M = map(int, sys.stdin.readline().split())
MAXs = [(0, '') for _ in range(M)]
CNT = [{'A':0, 'T':0, 'G':0, 'C':0} for _ in range(M)]
DISTANCE = 0

for i in range(N):
    DNA = sys.stdin.readline()
    for j in range(M):
        CNT[j][DNA[j]] += 1
        if MAXs[j][0] < CNT[j][DNA[j]] or (MAXs[j][0] == CNT[j][DNA[j]] and DNA[j] < MAXs[j][1]):
            MAXs[j] = (CNT[j][DNA[j]], DNA[j])

for i in range(M):
    DISTANCE += N - MAXs[i][0]
    print(MAXs[i][1], end='')
print(f'\n{DISTANCE}')