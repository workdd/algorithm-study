def NAndM(ans, n, m, deep):
    if deep == m:
        for k in ans:
            print(k, end=' ')
        print()
        return
    for i in range(1, n+1):
        ans.append(i)
        NAndM(ans, n, m, deep+1)
        del ans[-1]
        
n, m = map(int, input().split())
NAndM([], n, m, 0)

