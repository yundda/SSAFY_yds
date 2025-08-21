T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    K = N // 2
    cnt = 0
    for i in range(K + 1):
        for j in range(-i, i + 1):
            cnt += arr[i][K - j]
            print(arr[i][K - j])
            if i != K:
                cnt += arr[N - 1 - i][K - j]
                print(arr[N - 1 - i][K - j])

    print(f"#{t} {cnt}")
