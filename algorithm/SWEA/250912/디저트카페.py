import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deserts = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * 101
    used = [[False] * N for _ in range(N)]
    dr = [1,1,-1,-1]
    dc = [-1,1,1,-1]
    max_cnt = -1
    path = []

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N
    
    def recur(start_r,start_c,now_r,now_c,now_d,cnt):
        global max_cnt
        if now_d == 4:
            return
        
        nxt_r = now_r + dr[now_d]
        nxt_c = now_c + dc[now_d]

        if now_d == 3 and nxt_r == start_r and nxt_c == start_c:
            if max_cnt < cnt:
                max_cnt = cnt
            return
        
        # if now_d == 2 and now_r - start_r == now_c - start_c:
        #     while True:
        #         now_r -= 1
        #         now_c -= 1
        #         if now_r==start_r and now_c==start_c:
        #             if max_cnt < cnt:
        #                 max_cnt = cnt
        #             return
                
        #         if not in_range(now_r,now_c) or visited[deserts[now_r][now_c]]:
        #             return
        #         visited[deserts[now_r][now_c]] = True
        #         used[now_r][now_c] = True
        #         path.append(deserts[now_r][now_c])
        #         cnt += 1
                

        if not in_range(nxt_r,nxt_c):
            return
        if visited[deserts[nxt_r][nxt_c]]:
            return
        visited[deserts[nxt_r][nxt_c]] = True
        used[nxt_r][nxt_c] = True
        path.append(deserts[nxt_r][nxt_c])
        # 방향 그대로 전진
        recur(start_r,start_c,nxt_r,nxt_c,now_d,cnt+1)
        # 방향 바꿔서 전진
        recur(start_r,start_c,nxt_r,nxt_c,now_d + 1,cnt+1)
        path.pop()
        visited[deserts[nxt_r][nxt_c]] = False
        used[nxt_r][nxt_c] = False



    for i in range(N-2):
        for j in range(1,N-1):
            used[i][j] = True
            visited[deserts[i][j]] = True
            path.append(deserts[i][j])
            recur(i,j,i,j,0,1)
            path.pop()
            visited[deserts[i][j]] = False
            used[i][j] = False

    print(f'#{tc} {max_cnt}')




###################################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deserts = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * 101
    dr = [1,1,-1,-1]
    dc = [-1,1,1,-1]
    max_cnt = -1

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N
    
    def recur(start_r,start_c,now_r,now_c,now_d,cnt):
        global max_cnt
        if now_d == 4:
            return
        
        nxt_r = now_r + dr[now_d]
        nxt_c = now_c + dc[now_d]

        if now_d == 3 and nxt_r == start_r and nxt_c == start_c:
            if max_cnt < cnt:
                max_cnt = cnt
            return

        if not in_range(nxt_r,nxt_c):
            return
        
        if visited[deserts[nxt_r][nxt_c]]:
            return
        
        visited[deserts[nxt_r][nxt_c]] = True
        # 방향 그대로 전진
        recur(start_r,start_c,nxt_r,nxt_c,now_d,cnt+1)
        # 방향 바꿔서 전진
        recur(start_r,start_c,nxt_r,nxt_c,now_d + 1,cnt+1)
        visited[deserts[nxt_r][nxt_c]] = False

        
    for i in range(N-2):
        for j in range(1,N-1):
            visited[deserts[i][j]] = True
            recur(i,j,i,j,0,1)
            visited[deserts[i][j]] = False

    print(f'#{tc} {max_cnt}')