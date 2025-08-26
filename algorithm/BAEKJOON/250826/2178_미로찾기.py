N,M = map(int,input().split())
A = [list(map(int,list(input()))) for _ in range(N)]

Q = []
dr = [0,0,-1,1]
dc = [-1,1,0,0]
cnt = 0

visited = [[False] * M for _ in range(N)]

def in_range(r,c):
    return 0 <= r < N and 0 <= c < M

def bfs(i,j):
    cnt = 0
    Q.append((i,j))
    while Q:
        r,c = Q.pop(0)
        if r == N -1 and c == M -1:
            break
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if in_range(nr,nc) and A[nr][nc] == 1:
                Q.append((nr,nc))
                A[nr][nc] = A[r][c] + 1
    return A[N-1][M-1]


ans = bfs(0,0)
print(ans)     
     