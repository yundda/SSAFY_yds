N, M = map(int,input().split())

A = [0] * M
visited = [False] * (N + 1)

def dfs(cnt):
    if cnt == M:
        print(*A)
        return


    for n in range(1,N+1):
        if not visited[n]:
            visited[n] = True
            A[cnt] = n  # list 하나로 관리!!
            dfs(cnt + 1)
            visited[n] = False


dfs(0)