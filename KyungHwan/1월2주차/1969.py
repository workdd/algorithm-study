N, M = map(int, input().split())
DNAs = []

for _ in range(N):
    DNA = input()
    DNAs.append(DNA)


count_dict = {}

count = 0
for i in range(M):
    for j in range(N):
        count_dict[DNAs[j][i]] = count_dict.get(DNAs[j][i], 0) + 1
    count_dict = dict(sorted(count_dict.items()))
    max_dna = max(count_dict, key=count_dict.get)
    for j in range(N):
        if DNAs[j][i] != max_dna:
            count += 1
    print(max_dna, end="")
    count_dict = {}
print()
print(count)
