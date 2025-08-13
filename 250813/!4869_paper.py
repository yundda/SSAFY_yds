## dp 방식 사용

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    memo = [0] * 301
    memo[10] = 1
    memo[20] = 3

    for i in range(30, N + 1):
        memo[i] = memo[i - 10] + memo[i - 20] * 2

    print(f"#{t} {memo[N]}")

## 재귀 + memoization 사용

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    memo = [0] * 301
    memo[10] = 1
    memo[20] = 3

    def my_func(N):
        if N >= 30 and memo[N] == 0:
            memo[N] = dp(N - 10) + dp(N - 20) * 2
        return memo[N]

    ans = my_func(N)

    print(f"#{t} {ans}")


## 재귀함수 사용
T = int(input())
for t in range(1, T + 1):
    N = int(input())

    def my_func(N):
        if N >= 30:
            return my_func(N - 10) + my_func(N - 20) * 2
        elif N == 20:
            return 3
        elif N == 10:
            return 1

    ans = my_func(N)

    print(f"#{t} {ans}")
