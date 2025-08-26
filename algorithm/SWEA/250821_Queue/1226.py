T = 1
N = 16
for _ in range(T):
    t = int(input())
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
        visited = [[False] * N for _ in range(N)]
        q = []
        q.append((i, j))

        while q:
            r, c = q.pop(0)
            for k in range(4):
                n_r = r + dr[k]
                n_c = c + dc[k]
                if in_range(n_r, n_c) and A[n_r][n_c] != 1 and not visited[n_r][n_c]:
                    if A[n_r][n_c] == 3:
                        return True
                    visited[n_r][n_c] = True
                    q.append((n_r, n_c))
        return False

    ans = 1 if BFS(s_i, s_j) else 0

    print(f"#{t} {ans}")
