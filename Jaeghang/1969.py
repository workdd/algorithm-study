import sys

N, M = map(int, sys.stdin.readline().split())

ALPHA = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

str_lst = []
answer = ""
answer_cnt = 0
for _ in range(N):
    st = sys.stdin.readline()
    str_lst.append(st)

for m in range(M):
    alpha = ALPHA.copy()
    for n in range(N):
        key = str_lst[n][m]

        alpha[key] += 1
    val = max(alpha, key=alpha.get)
    answer += val
    answer_cnt += N - alpha[val]

print(answer)
print(answer_cnt)
