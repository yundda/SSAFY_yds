import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(lambda x: int(x)* 0.01 ,input().split())) for _ in range(N)]


    visited = [False] * N

    max_p = 0
    def recur(row,p):
        global max_p
        if row == N:
            max_p = p
            return
        for col in range(N):
            if visited[col] or P[row][col] == 0:
                continue
            if max_p > p * P[row][col]:
                continue
            visited[col] = True
            recur(row+1,p * P[row][col])
            visited[col] = False
            



    recur(0,1)
    max_p *= 100
    
    print(f'#{tc} {max_p:.6f}')