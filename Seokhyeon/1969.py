n, m = map(int, input().split())

dnas = []
result = ''
hamming_distance = 0

for i in range(n):
    dnas.append(input())

for i in range(m):
    ACGT = [0, 0, 0, 0]
    for j in range(n):
        if dnas[j][i] == 'A':
            ACGT[0] += 1
        elif dnas[j][i] == 'C':
            ACGT[1] += 1
        elif dnas[j][i] == 'G':
            ACGT[2] += 1
        elif dnas[j][i] == 'T':
            ACGT[3] += 1

    max_dna = max(ACGT)
    max_index = ACGT.index(max_dna)

    if max_index == 0:
        result += 'A'
    elif max_index == 1:
        result += 'C'
    elif max_index == 2:
        result += 'G'
    elif max_index == 3:
        result += 'T'

    hamming_distance += n - max_dna

print(result)
print(hamming_distance)
