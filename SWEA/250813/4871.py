T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    A = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        A[a][b] = True

    start, end = map(int, input().split())

    visited = [0] * (V + 1)

    def dfs(s, e):
        if visited[e]:
            return 1
        visited[s] = 1
        for n in range(1, V + 1):
            if not visited[n] and A[s][n]:
                dfs(n, e)

        return visited[e]

    ans = dfs(start, end)

    print(f"#{t} {ans}")
