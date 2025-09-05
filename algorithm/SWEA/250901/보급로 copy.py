import heapq

T = int(input())
for t in range(1,T+1):
    N = int(input())
    A = [list(map(int,list(input()))) for _ in range(N)]

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    
    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    INF = 10**10
    dist = [[INF] *N for _ in range(N)]
    def Da():
        q = []
        heapq.heappush(q,(dist[0][0],0,0))

        while q:
            d,r,c = heapq.heappop(q)
            if r == N-1 and c == N-1:
                return 
            if d > dist[r][c]:
                continue
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr,nc):
                    if dist[nr][nc] > A[nr][nc] + d:
                        dist[nr][nc] = A[nr][nc] + d
                        heapq.heappush(q,(dist[nr][nc],nr,nc))

    dist[0][0] = 0
    Da()

    print(f'#{t} {dist[N-1][N-1]}')