T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_sum = 10**3

    def f(row, sum):
        global min_sum
        if row == N and min_sum > sum:
            min_sum = sum
            return
        if sum > min_sum:
            return
        for col in range(N):
            if not visited[col]:
                visited[col] = True
                f(row + 1, sum + arr[row][col])
                visited[col] = False

    f(0, 0)

    print(f"#{t} {min_sum}")
