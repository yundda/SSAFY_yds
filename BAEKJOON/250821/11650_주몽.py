# 구간 합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum_nums = [0] * (N + 1)

sum_nums[0] = 0
for i in range(N):
    sum_nums[i] = sum_nums[i - 1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_nums[j - 1] - sum_nums[i - 2])
