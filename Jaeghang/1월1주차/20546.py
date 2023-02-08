money = int(input())

stock_list = list(map(int, input().split()))

days = 14

BNP = [money, 0]
TIMING = [money, 0]

flow_down_cnt = 0
flow_up_cnt = 0

idx = 0
for day, price in enumerate(stock_list):
    if BNP[0] >= price:
        stock_num = BNP[0] // price
        BNP[0] -= stock_num * price
        BNP[1] += stock_num

    if day > 0:
        if price > stock_list[day - 1]:
            flow_up_cnt += 1
            flow_down_cnt = 0
        elif price < stock_list[day - 1]:
            flow_down_cnt += 1
            flow_up_cnt = 0

        else:
            flow_up_cnt = 0
            flow_down_cnt = 0

        if flow_down_cnt >= 3 and TIMING[0] >= price:
            stock_num = TIMING[0] // price
            TIMING[0] -= stock_num * price
            TIMING[1] += stock_num

        if flow_up_cnt >=3 and TIMING[1] > 0:
            TIMING[0] += TIMING[1] * price
            TIMING[1] = 0

BNP_money = BNP[0] + BNP[1] * stock_list[-1]
TIMING_money = TIMING[0] + TIMING[1] * stock_list[-1]

if BNP_money > TIMING_money:
    print("BNP")
elif BNP_money < TIMING_money:
    print("TIMING")
else:
    print("SAMESAME")