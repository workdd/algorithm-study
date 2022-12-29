N, M = map(int,input().split())

def loop(st):
    s = st
    if len(s) == M*2:
        print(s)
        return True

    else:
        for i in range(1,N+1):
            s = st
            s = s + str(i) + " "
            loop(s)

loop("")
