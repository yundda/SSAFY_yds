T = int(input())
for t in range(1, T + 1):
    N = int(input())
    area = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if area[i][j] == "2":
                s_i, s_j = i, j
    visited = [[0] * N for _ in range(N)]
    stack = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    def connected(i, j):
        if 0 <= i < N and 0 <= j < N:
            if area[i][j] != "1":
                return True
        return False

    def find_road(s_i, s_j):
        visited[s_i][s_j] = 1
        stack.append((s_i, s_j))
        while stack:
            v_i, v_j = stack.pop()
            if area[v_i][v_j] == "3":
                return 1
            for p in range(4):
                ni = v_i + dr[p]
                nj = v_j + dc[p]
                if connected(ni, nj) and visited[ni][nj] != 1:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))

        return 0

    ans = find_road(s_i, s_j)

    print(f"#{t} {ans}")
