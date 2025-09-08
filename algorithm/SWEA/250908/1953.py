import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    hole = [list(map(int,input().split())) for _ in range(N)]


    dic = { 0:'상', 1:'좌', 2: '하', 3: '우'}
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

    def pos(nr,nc,nst,l):
        global ans
        if l == L:
            return

        for k in structure_type[nst]:
            r = nr + dr[k]
            c = nc + dc[k]
            if in_range(r,c):
                st = hole[r][c]
                if not visited[r][c] and st != 0 and is_connect((k+2)%4,st):
                    visited[r][c] = True
                    ans += 1
                    pos(r,c,st,l+1)

        

    ans = 1
    visited[R][C] = True
    pos(R,C,hole[R][C],1)

    
    print(f'#{t} {ans}')