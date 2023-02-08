import sys

N = int(input())

min_dp = [0 for _ in range(101)]

min_num = {
    2: 1,
    3: 7,
    4: 4,
    5: 2,
    6: 0,
    7: 8
}

for _ in range(N):
    n = int(input())
    ans = ""
    if n == 6:
        print("6", end=" ")
    else:
        for idx in range(2, n + 1):
            min_val = ""
            if idx in min_num:
                min_dp[idx] = min_num[idx]
                continue
            for loop in range((idx // 2) - 1):
                left = loop + 2
                right = idx - left

                val_left = min_dp[left]
                val_right = min_dp[right]

                if left == right and val_left != 0 and val_right != 0:
                    val = int(str(min_dp[left]) * 2)
                elif val_left == 0:
                    val = str(val_right).split()
                    val.insert(1, '0')
                    val = int(''.join(val))

                    val2 = int('6' + str(val_right))

                    val = min(val, val2)
                elif val_right == 0:
                    val = str(val_left).split()
                    val.insert(1, '0')
                    val = int(''.join(val))

                elif int(str(val_left)[0]) > int(str(val_right)[0]):
                    val = int(str(val_right) + str(val_left))
                else:
                    val = int(str(val_left) + str(val_right))
                if val == 0:
                    continue
                if min_val == "":
                    min_val = val
                elif min_val > val:
                    min_val = val
                min_dp[idx] = min_val
        print(min_dp[n], end=" ")

    cnt = n // 2

    if n % 2 == 0:
        print('1' * cnt)
    else:
        print('7' + '1' * (cnt - 1))
