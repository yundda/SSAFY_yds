T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    M = 4
    arr = [[0] * N for _ in range(M)]

    for k in range(1, K + 1):
        for i in range(M):
            for j in range(N):
                if (i + j + 1) % k == 0:
                    arr[i][j] = 0 if arr[i][j] == 1 else 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            cnt += arr[i][j]

    print(f"#{t} {cnt}")
