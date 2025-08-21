T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] == 2:
                s_i = i
                s_j = j

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    def in_range(r, c):
        return 0 <= r < N and 0 <= c < N

    def BFS(i, j):
        visited = [[0] * N for _ in range(N)]
        q = []
        visited[i][j] = 0
        q.append((i, j))
        while q:
            r, c = q.pop(0)
            for k in range(4):
                n_r = r + dr[k]
                n_c = c + dc[k]
                if in_range(n_r, n_c) and A[n_r][n_c] != 1 and visited[n_r][n_c] == 0:
                    visited[n_r][n_c] = visited[r][c] + 1
                    if A[n_r][n_c] == 3:
                        return visited[n_r][n_c] - 1
                    q.append((n_r, n_c))
        return 0

    ans = BFS(s_i, s_j)

    print(f"#{t} {ans}")
