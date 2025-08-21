T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    res = [0] * N

    min_val = 10**3

    def f(i, s):
        global min_val
        if s >= min_val:
            return
        if i == N and min_val > s:
            min_val = s
            return
        for j in range(N):
            if not visited[j]:
                visited[j] = True  # 방문 안 했던 열에 대해서 방문처리
                k = arr[i][j]  # 현재 행(i) 방문 안 한 열(j) 값
                f(i + 1, s + k)  # 다음 행에 대해 연산 시작, 현재 행까지의 합 전달
                visited[j] = (
                    False  # 모든 행에 대한 연산 끝났으면, 다른 행 계산해야하니까
                )

    f(0, 0)
    print(f"#{t} {min_val}")
