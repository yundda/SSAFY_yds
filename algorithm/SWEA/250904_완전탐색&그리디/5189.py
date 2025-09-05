import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    visited = [False] * (N)
    min_usage = 10**10

    def find_route(n,now,usage):
        global min_usage
        if min_usage < usage:
            return
        
        if n == N-1:
            usage += B[now][0]
            if min_usage > usage:
                min_usage = usage
            return
        
        for i in range(1,N):
            if not visited[i]:
                visited[i] = True
                find_route(n+1,i,usage + B[now][i])
                visited[i] = False
    
    B = [list(map(int,input().split())) for _ in range(N)]
    
    visited[0] = True
    find_route(0,0,0)

    print(f'#{t} {min_usage}')