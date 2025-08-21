T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 0
    cnt = 0
    while True:
        if cnt == M:
            break
        idx = (idx + 1) % N
        cnt += 1

    ans = nums[idx]

    print(f"#{t} {ans}")
