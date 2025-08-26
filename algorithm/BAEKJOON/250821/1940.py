#### 투포인터 ####
N = int(input())
M = int(input())
nums = list(map(int, input().split()))

i, j, total, cnt = 0, N - 1, 0, 0

nums.sort()

while i != j:
    total = nums[i] + nums[j]
    if total == M:
        cnt += 1
        i += 1
        # j = N - 1
        j -= 1
    elif total > M:
        j -= 1
    else:  # total < M
        i += 1

print(cnt)
