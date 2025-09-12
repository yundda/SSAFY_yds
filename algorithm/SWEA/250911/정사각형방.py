import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(N)]



    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    max_cnt = 0
    min_val = N * N
    visited = [[0] * N for _ in range(N)]

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N


    def visit_room(r,c):
        cnt = 0
        if visited[r][c] != 0:
            return 0
        visited[r][c] = 1
        while True:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if not in_range(nr,nc):
                    continue
                    
                if A[nr][nc] == A[r][c] + 1:
                    if visited[nr][nc] > visited[r][c] + 1:
                        continue
                    visited[nr][nc] = visited[r][c] + 1
                    if cnt <= visited[nr][nc]:
                        cnt = visited[nr][nc]
                        r = nr
                        c = nc
                        break
            else:
                return cnt
        return cnt


    for i in range(N):
        for j in range(N):
            if A[i][j] != N*N:
                cnt = visit_room(i,j)
                if max_cnt < cnt or (max_cnt == cnt and min_val > A[i][j]):
                    max_cnt = cnt
                    min_val = A[i][j]


    print(f'#{tc}', min_val, max_cnt)