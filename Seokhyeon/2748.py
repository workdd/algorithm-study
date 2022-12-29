fib_list = [-1 for i in range(100)]
fib_list[0] = 0
fib_list[1] = 1


def fibo(num):
    if fib_list[num] >= 0:
        return fib_list[num]

    fib_list[num] = fibo(num-1) + fibo(num-2)
    return fib_list[num]


n = int(input())
print(fibo(n))
