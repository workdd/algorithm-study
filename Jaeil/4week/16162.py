import sys

N, A, D = map(int, sys.stdin.readline().strip().split())
melodies = list(map(int, sys.stdin.readline().strip().split()))

ans = 0

for melody in melodies:
    if melody == A + D * ans:
        ans+=1

print(ans)