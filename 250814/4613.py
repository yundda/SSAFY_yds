T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]

    C = [[] for _ in range(N)]
    for i in range(N):
        w, r, b = 0, 0, 0
        for j in range(M):
            if A[i][j] == "W":
                w += 1
            elif A[i][j] == "B":
                b += 1
            else:
                r += 1
        C[i].append(w)
        C[i].append(r)
        C[i].append(b)

    def chg_color(x, y):
        cnt = 0
        for i in range(x + 1):
            cnt += C[i][1] + C[i][2]
        for j in range(x + 1, y + 1):
            cnt += C[j][0] + C[j][1]
        for k in range(y + 1, N):
            cnt += C[k][0] + C[k][2]
        return cnt

    min_val = N * M
    for x in range(N - 2):
        for y in range(x + 1, N - 1):
            val = chg_color(x, y)
            if min_val > val:
                min_val = val

    print(f"#{t} {min_val}")
