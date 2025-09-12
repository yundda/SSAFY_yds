import sys
from collections import deque
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    hole = [list(map(int,input().split())) for _ in range(N)]


    dr = (-1,0,1,0)
    dc = (0,-1,0,1)


    structure_type = [[-1], [0,1,2,3], [0,2], [1,3], [0,3], [2,3], [1,2], [0,1]]
    visited = [[False] * M for _ in range(N)]
    
    def in_range(r,c):
        return 0 <= r < N and 0 <= c < M

    def is_connect(d,st):
        if d in structure_type[st]:
            return True
        return False

    q = deque()
    q.append((R,C))
    route = [[0] * M for _ in range(N)]
    route[R][C] = 1

    ans = 1
    while q:
        nr, nc = q.popleft()
        if route[nr][nc] == L:
            break
        for k in structure_type[hole[nr][nc]]:
            r = nr + dr[k]
            c = nc + dc[k]
            if in_range(r,c):
                st = hole[r][c]
                if route[r][c] == 0 and st != 0 and is_connect((k+2)%4,st):
                    q.append((r,c))
                    route[r][c] = route[nr][nc] + 1
                    ans += 1


    print(f'#{t} {ans}')