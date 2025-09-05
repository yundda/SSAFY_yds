T = int(input())
for t in range(1,T+1):
    N, K = map(int,input().split())
    M = [list(map(int,input().split())) for _ in range(N)]

    visited = [[False] *N for _ in range(N)]
    highest = 0
    hidx = []
    for m in M:
        for h in m:
            if highest < h:
                highest = h

    for i in range(N):
        for j in range(N):
            if M[i][j] == highest:
                hidx.append((i,j))

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    max_road = 0

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    def DFS(now_r,now_c, cnt,is_cutting):
        global max_road
        if max_road < cnt:
            max_road = cnt

        for k in range(4):
            nxtr = now_r + dr[k]
            nxtc = now_c + dc[k]
            if in_range(nxtr,nxtc) and not visited[nxtr][nxtc]:
                if M[nxtr][nxtc] < M[now_r][now_c]:
                    visited[nxtr][nxtc] = True
                    DFS(nxtr,nxtc,cnt+1,is_cutting)
                    visited[nxtr][nxtc] = False
                elif not is_cutting and M[nxtr][nxtc] - M[now_r][now_c] < K:
                    origin = M[nxtr][nxtc]
                    M[nxtr][nxtc] = M[now_r][now_c] - 1
                    visited[nxtr][nxtc] = True
                    DFS(nxtr,nxtc,cnt+1, True)
                    M[nxtr][nxtc] = origin
                    visited[nxtr][nxtc] = False 
                    break
        return

    for i,j in hidx:
        visited[i][j] = True
        DFS(i,j,1,False)
        visited[i][j] = False

    print(f'#{t} {max_road}')

