from heapq import heappop,heappush
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    INF = 10**10
    dist = [[INF] * N for _ in range(N)]

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N
    
    def dijkstra():
        hq = [(0,0,0)]
        dist[0][0] = 0

        while hq:
            d,r,c = heappop(hq)
            if d > dist[r][c]:
                continue
            for k in range(4):
                nxt_r = r + dr[k]
                nxt_c = c + dc[k]
                if not in_range(nxt_r,nxt_c):
                    continue

                if area[r][c] < area[nxt_r][nxt_c]:
                    new_d = d + area[nxt_r][nxt_c] - area[r][c] + 1
                else:
                    new_d = d + 1

                if dist[nxt_r][nxt_c] <= new_d:
                    continue
                dist[nxt_r][nxt_c] = new_d
                heappush(hq,(new_d,nxt_r,nxt_c))
        return
    
    dijkstra()
    result = dist[N-1][N-1]

    print(f'#{tc} {result}')