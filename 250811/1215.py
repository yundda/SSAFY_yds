# T = int(input())
T = 1
for t in range(1, T + 1):
    N = int(input())
    print(N)
    M = 8
    arr = [list(input()) for _ in range(M)]

    def count(a):
        cnt = 0
        for i in range(M - N + 1):
            for p in range(int(N / 2)):
                if a[i + p] != a[i + N - 1 - p]:
                    break
            else:
                cnt += 1
        return cnt

    cnt = 0
    # 행 검사
    for i in range(M):
        a = [arr[i][j] for j in range(M)]
        cnt += count(a)

    # 열 검사
    for j in range(M):
        a = [arr[i][j] for i in range(M)]
        cnt += count(a)

    print(f"#{t} {cnt}")
