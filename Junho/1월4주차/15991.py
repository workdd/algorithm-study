import sys
input = sys.stdin.readline

DP = [1, 2, 2, 3, 3, 6]

# dp 채우기
for i in range(6, 100_000):
    DP.append((DP[i-2] + DP[i-4] + DP[i-6]) % 1_000_000_009)
    
# 출력
for _ in range(int(input())):
    n = int(input())
    print(DP[n-1])