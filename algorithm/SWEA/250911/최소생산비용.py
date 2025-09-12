import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int,input().split())) for _ in range(N)]


    visited = [False] * N
    INF = 10**10
    min_cost = INF
    def recur(row, cost):
        global min_cost
        if row == N:
            min_cost = cost
            return
        
        for col in range(N):
            if visited[col]:
                continue
            if min_cost < cost + V[row][col]:
                continue
            visited[col] = True
            recur(row+1, cost + V[row][col])
            visited[col] = False

    recur(0,0)

    print(f'#{tc}', min_cost)