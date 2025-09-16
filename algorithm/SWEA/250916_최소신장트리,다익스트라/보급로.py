import sys
from heapq import heappop,heappush
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int,list(input()))) for _ in range(N)]
    INF = 10**10
    costs = [[INF]*N for _ in range(N)]

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N 

    def BFS():
        hq = []
        costs[0][0] = 0
        heappush(hq,(0,0,0))

        while hq:
            cost,r,c = heappop(hq)
            if cost > costs[r][c]:
                continue
            for k in range(4):
                nxt_r = r + dr[k]
                nxt_c = c + dc[k]
                if not in_range(nxt_r,nxt_c):
                    continue
                new_cost = cost + M[nxt_r][nxt_c]
                if costs[nxt_r][nxt_c] <= new_cost:
                    continue
                costs[nxt_r][nxt_c] = new_cost
                heappush(hq,(costs[nxt_r][nxt_c],nxt_r,nxt_c))



    BFS()
    print(f'#{tc} {costs[N-1][N-1]}')