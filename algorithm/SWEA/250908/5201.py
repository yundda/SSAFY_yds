import sys
sys.stdin = open('input.txt','r')
import heapq

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    weights = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    
    # weights.sort(reverse = True)
    trucks.sort(reverse = True)

    ans = 0
    q = []
    for w in weights:
        heapq.heappush(q,-w)

    for t in trucks:
        w = heapq.heappop(q)
        w = -w
        if t >= w:
            ans += w 
        else:
            heapq.heappush(q,-w)


    print(f'#{tc} {ans}')