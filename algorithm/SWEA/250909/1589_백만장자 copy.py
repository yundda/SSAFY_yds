import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    prices = list(map(int,input().split()))

    max_price = 0
    earn = 0
    for i in range(N-1,-1,-1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            earn += (max_price - prices[i])

        
    print(f'#{tc} {earn}')