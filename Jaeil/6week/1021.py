n, m = map(int, input().split())
q = list(map(int, input().split()))
ans = 0
for i in range(m):
    left = 1
    right = n
    mid = (left + right) // 2
    while q[i] != mid:
        if q[i] < mid:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
        ans += 1
print(ans)
