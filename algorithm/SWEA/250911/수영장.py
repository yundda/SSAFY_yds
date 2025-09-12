import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    fee = list(map(int,input().split()))
    plans = list(map(int,input().split()))
    prices = [0] * 14


    for m in range(12):
        price = fee[0] * plans[m]
        prices[m] = min(price,fee[1])

    min_price = 10**10
    def three_month(m,sum_price):
        global min_price
        if m > 11:
            if min_price > sum_price:
                min_price = sum_price
            return


        if prices[m] + prices[m+1] + prices[m+2] > fee[2]:
            three_month(m+3,sum_price+fee[2])

        three_month(m+1,sum_price+prices[m])
    
    three_month(0,0)
    min_price = min(min_price, fee[3])
    print(f'#{tc} {min_price}')