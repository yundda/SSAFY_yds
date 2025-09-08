import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    weights = list(map(int,input().split()))
    used = [False] * N
    trucks = list(map(int,input().split()))
    
    weights.sort(reverse = True)
    trucks.sort(reverse = True)

    ans = 0
    for t in trucks:
        for i in range(N):
            if  not used[i] and t >= weights[i]:
                ans += weights[i]
                used[i] = True
                break


    print(f'#{tc} {ans}')