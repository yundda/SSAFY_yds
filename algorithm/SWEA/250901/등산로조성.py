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
    stack = []
    max_road = 0

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    def DFS(cnt,is_cutting):
        global max_road
        if max_road < cnt:
            max_road = cnt

        now_r,now_c = stack.pop()

        for k in range(4):
            nxtr = now_r + dr[k]
            nxtc = now_c + dc[k]
            if in_range(nxtr,nxtc) and not visited[nxtr][nxtc]:
                if M[nxtr][nxtc] < M[now_r][now_c]:
                    visited[nxtr][nxtc] = True
                    stack.append((nxtr,nxtc))
                    DFS(cnt+1,is_cutting)
                    visited[nxtr][nxtc] = False
                elif not is_cutting and M[nxtr][nxtc] - M[now_r][now_c] < K:
                    for cut in range(1,K+1):
                        if M[nxtr][nxtc] - cut < M[now_r][now_c]:
                            visited[nxtr][nxtc] = True
                            M[nxtr][nxtc] -= cut
                            stack.append((nxtr,nxtc))
                            DFS(cnt+1, not is_cutting)
                            M[nxtr][nxtc] += cut
                            visited[nxtr][nxtc] = False 
                            break
        return

    ans = 0
    for i,j in hidx:
        stack.append((i,j))
        visited[i][j] = True
        DFS(1,False)
        visited[i][j] = False

        if ans < max_road:
            ans = max_road
        

    print(f'#{t} {ans}')