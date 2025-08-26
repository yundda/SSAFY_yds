T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{t}")
    for k in range(N):
        for i in range(N - 1, -1, -1):
            print(arr[i][k], end="")
            if i == 0:
                print("", end=" ")

        for j in range(N - 1, -1, -1):
            print(arr[N - 1 - k][j], end="")
            if j == 0:
                print("", end=" ")

        for i in range(N):
            print(arr[i][N - 1 - k], end="")
            if i == N:
                print("", end=" ")
        print()
