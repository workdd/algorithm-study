MONEY = int(input())
STOCK = list(map(int, input().split()))

BNP_MONEY = TIMING_MONEY = MONEY
BNP_STOCK = TIMING_STOCK = 0
TIMING_CONTINUOS = 0

for i in range(len(STOCK)):
    BNP_STOCK += BNP_MONEY // STOCK[i]
    BNP_MONEY %= STOCK[i]
    if i==0:
        continue
    if STOCK[i-1] < STOCK[i]:
        if TIMING_CONTINUOS < 0:
            TIMING_CONTINUOS = 0
        TIMING_CONTINUOS += 1
        if TIMING_CONTINUOS == 3:
            TIMING_MONEY += STOCK[i] * TIMING_STOCK
            TIMING_STOCK = 0
    elif STOCK[i-1] > STOCK[i]:
        if TIMING_CONTINUOS > 0:
            TIMING_CONTINUOS = 0
        TIMING_CONTINUOS -= 1
        if TIMING_CONTINUOS == -3:
            TIMING_STOCK += TIMING_MONEY // STOCK[i]
            TIMING_MONEY %= STOCK[i]
    else:
        TIMING_CONTINUOS = 0

BNP_TOTAL = BNP_MONEY + BNP_STOCK * STOCK[-1]
TIMING_TOTAL = TIMING_MONEY + TIMING_STOCK * STOCK[-1]

if BNP_TOTAL > TIMING_TOTAL:
    print("BNP")
elif BNP_TOTAL < TIMING_TOTAL:
    print("TIMING")
else:
    print("SAMESAME")
