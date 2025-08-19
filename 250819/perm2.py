T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    min_val = 10**18

    visited = [False] * N
    res = [0] * N

    min_val = 10**18

    def f(i, s):
        global min_val
        if s >= min_val:
            return
        if i == N and min_val > s:
            min_val = s
            return
        for j in range(N):
            if not visited[j]:
                visited[j] = True
                k = arr[i][j]
                f(i + 1, s + k)
                visited[j] = False

    f(0, 0)
    print(f"#{t} {min_val}")
