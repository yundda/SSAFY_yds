from collections import deque
import heapq
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    # val = [[0]*N for _ in range(N)]
    # val[0][0] = board
    min_val = 10**10
    dr = [0,1]
    dc = [1,0]

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N
    
    q = []
    heapq.heappush(q,(board[0][0],0,0))
    visited[0][0] = True
    while q:
        nv, nr,nc = heapq.heappop(q)

        if nr == N-1 and nc == N-1:
            break
        
        for k in range(2):
            r = nr+dr[k]
            c = nc+dc[k]
            if in_range(r,c) and not visited[r][c]:
                visited[r][c] = True
                board[r][c] += nv
                heapq.heappush(q,(board[r][c],r,c))
                
    

    print(f'#{t} {board[N-1][N-1]}')