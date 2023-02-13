import sys

N, K = map(int, sys.stdin.readline().split())

start = end = 0

nums = list(map(int, sys.stdin.readline().split()))

MAX = max(nums) + 1
cnt = [0 for n in range(MAX)]

ans = 0
while end < len(nums):
    end_num = nums[end]
    start_num = nums[start]
    cnt[end_num] += 1
    if cnt[end_num] > K:
        cnt[end_num] -= 1
        cnt[start_num] -= 1
        sum = end - start
        ans = max(sum, ans)
        start += 1
    else:
        end += 1

sum = end - start
ans = max(sum, ans)
print(ans)
