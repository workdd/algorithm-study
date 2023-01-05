def a_1(num):
    for a in range(1, num+1):
        print(a)

def a_2(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            print(a, b)

def a_3(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            for c in range(1, num+1):
                print(a, b, c)

def a_4(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            for c in range(1, num+1):
                for d in range(1, num+1):
                    print(a, b, c, d)

def a_5(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            for c in range(1, num+1):
                for d in range(1, num+1):
                    for e in range(1, num+1):
                        print(a, b, c, d, e)

def a_6(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            for c in range(1, num+1):
                for d in range(1, num+1):
                    for e in range(1, num+1):
                        for f in range(1, num+1):
                             print(a, b, c, d, e, f, )

def a_7(num):
    for a in range(1, num+1):
        for b in range(1, num+1):
            for c in range(1, num+1):
                for d in range(1, num+1):
                    for e in range(1, num+1):
                        for f in range(1, num+1):
                            for g in range(1, num+1):
                                print(a, b, c, d, e, f, g)

functions = {
    1: a_1,
    2: a_2,
    3: a_3,
    4: a_4,
    5: a_5,
    6: a_6,
    7: a_7,
}

n, m = map(int, input().split())
func = functions[m]
func(n)