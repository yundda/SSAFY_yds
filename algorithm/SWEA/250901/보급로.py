import heapq
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    A = [list(map(int,list(input()))) for _ in range(N)]

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    visited = [[False] *N for _ in range(N)]
    
    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    ans = 10**10



    '''
    백트래킹으로 구현 x
    시간 복잡도 매우 큼
    -> 우선순위 큐 or 다익스트라
    '''
    ### 백트래킹
    # stack = []
    # def DFS(r,c,time):
    #     global ans
    #     if ans < time:
    #         return
    #     if r == N-1 and c == N-1:
    #         ans = time
    #         return        
    #     for k in range(4):
    #         nxtr = r + dr[k]
    #         nxtc = c + dc[k]
    #         if in_range(nxtr,nxtc) and not visited[nxtr][nxtc]:
    #             visited[nxtr][nxtc] = True
    #             DFS(nxtr,nxtc,time+A[nxtr][nxtc])
    #             visited[nxtr][nxtc] = False

    ### 우선순위 큐
    def BFS():
        global ans
        q = []
        heapq.heappush(q,(0,0,0))
        visited[0][0] = True
        while q:
            time, r,c = heapq.heappop(q)
            if r == N-1 and c == N-1:
                ans = time
                return 
            for k in range(4):
                nxtr = r + dr[k]
                nxtc = c + dc[k]
                if in_range(nxtr,nxtc) and not visited[nxtr][nxtc]:
                    if ans > time+A[nxtr][nxtc]:
                        heapq.heappush(q,(time+A[nxtr][nxtc],nxtr,nxtc))
                        visited[nxtr][nxtc] = True
                        A[nxtr][nxtc] += time
                    else:
                        continue

    BFS()

    print(f'#{t} {ans}')