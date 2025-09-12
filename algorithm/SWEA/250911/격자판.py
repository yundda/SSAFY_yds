import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = 4
    V = [list(map(int,input().split())) for _ in range(N)]

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    path = []
    diff = []

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    # cnt = 0
    # def recur(r,c,n):
    #     global cnt
    #     if n==3:
    #         print(*path)
    #         return

    #     for k in range(4):
    #         nr = r + dr[k]
    #         nc = c + dc[k]
    #         if not in_range(nr,nc):
    #             continue
    #         path.append((nr,nc))
    #         recur(nr,nc,n+1)
    #         path.pop()

    # for i in range(N):
    #     for j in range(N):
    #         print(f'{i},{j} 시작')
    #         path.append((i,j))
    #         recur(i,j,1)
    #         path.pop()

    print(f'#{tc}', min_cost)


    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N

    def counting(left, mid, right):
        if V[left] == V[right]:
            pass
        pass
    
    def partition(left, right):
        pass