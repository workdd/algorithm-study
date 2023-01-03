import sys

N = int(sys.stdin.readline())

num = 1

num_str = "1 2"
if N % 2 == 0:
    for _ in range(N // 2):
        print(num_str, end=" ")

else:
    for _ in range(N // 2):
        print(num_str, end=" ")

    print("3")

