

def BNP(cash, chart):
    # 주식 매수 종목 dict
    mesu_dict = {}

    # chart를 for 문으로 하나씩 돌며 살 수 있으면 무지성 매수
    for i in chart:
        if cash >= i:
            mesu_dict[i] = cash // i
            cash = cash % i

    # 매수 종목 수익률 확인
    suik = 0
    for j in mesu_dict:
        suik += chart[-1] * mesu_dict[j]

    # 현금과 더하여 리턴
    return (cash+suik)

def TIMING(cash, chart):
    mesu_dict = {}
    # 몇번 상승, 하강했는지 확인
    count = 0
    # 차트를 돌며 확인
    for i in range(1, len(chart)):
        # 전일 종가와 비교 오늘이 더 비싸면
        if chart[i] > chart[i-1]:
            # 만약 하강한 상태라면 다시 초기화
            if count < 0:
                count = 0
            # 상승에 +1
            count +=1
            # 만약 연속 3번 상승했다면
            if count >= 3 and mesu_dict:
                # 풀 매도
                for j in mesu_dict:
                    cash += chart[i] * mesu_dict[j]
                mesu_dict = {}

        # 전일 종가 비교 오늘이 더 싸면
        elif chart[i] < chart[i-1]:
            # 만약 상승한 상태라면 초기화
            if count > 0 :
                count = 0
            # 하강에 +1
            count -= 1

            #만약 3번 연속 하강했다면
            if count <= -3:
                #풀 매수
                if cash >= chart[i]:
                    mesu_dict[chart[i]] = cash // chart[i]
                    cash = cash % chart[i]
    # 장 종료 후 주식수익 계산
    suik = 0
    for j in mesu_dict:
        suik += chart[-1] * mesu_dict[j]
    # 현금과 더하여 리턴
    return (cash+suik)


cash = int(input())
chart = list(map(int, input().split()))

BNP_suik = BNP(cash, chart)
TIMING_suik = TIMING(cash, chart)


if BNP_suik > TIMING_suik:
    print("BNP")
elif BNP_suik < TIMING_suik:
    print("TIMING")
else:
    print("SAMESAME")