N = int(input())
nums = [int(input()) for _ in range(N)]
## 버블 정렬

for i in range(N - 1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for n in nums:
    print(n)

# 선택 정렬

for i in range(N - 1):
    min_idx = i
    for j in range(i + 1, N):
        if nums[min_idx] > nums[j]:
            min_idx = j
    nums[min_idx], nums[i] = nums[i], nums[min_idx]

for n in nums:
    print(n)
