T = 1
for _ in range(T):
    t = int(input())
    N = 8
    M = 5
    nums = list(map(int, input().split()))

    i = 1
    p = 0
    while True:
        nums[p] -= i
        if nums[p] <= 0:
            nums[p] = 0
            break
        i = i % M + 1
        p = (p + 1) % N

    ans = [nums[i % N] for i in range(p + 1, p + 1 + N)]

    print(f"#{t}", *ans)
