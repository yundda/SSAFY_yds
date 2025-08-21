T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_val = 10**3

    def f(i, s):
        global min_val
        if s > min_val:
            return
        if i == N and min_val > s:
            min_val = s
            return
        else:
            for j in range(i, N):
                p[i], p[j] = p[j], p[i]
                f(i + 1, s + arr[i][p[i]])
                p[i], p[j] = p[j], p[i]

    p = [i for i in range(N)]
    f(0, 0)
    print(f"#{t} {min_val}")
