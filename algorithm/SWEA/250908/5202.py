import sys
import heapq
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    q = []
    for _ in range(N):
        s, e = map(int,input().split())
        heapq.heappush(q,(e,s))

    
    ans = 1
    end,start = heapq.heappop(q)
    while q:
        n_e, n_s = heapq.heappop(q)
        if n_s >= end:
            end = n_e
            start = n_s
            ans += 1

    print(f'#{tc} {ans}')