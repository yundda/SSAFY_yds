# [투 포인터] 연속된 자연수의 합
###### 메모리 초과 #######
# N = int(input())

# sumArr = [0] * ((N + 1) // 2 + 1)
# for i in range(1, len(sumArr)):
#     sumArr[i] = sumArr[i - 1] + i

# cnt = 1
# for i in range(len(sumArr)):
#     if sumArr[i] >= N:
#         for j in range(1, i):
#             if sumArr[i] - sumArr[j - 1] < N:
#                 break
#             if sumArr[i] - sumArr[j - 1] == N:
#                 print(i, j)
#                 cnt += 1

# print(cnt)

#### 투 포인터 #####

N = int(input())
cnt = 0
start, end, total = 1, 1, 1

while start <= N:
    if total == N:
        cnt += 1
        total -= start
        start += 1

    if total > N:
        total -= start
        start += 1
    else:
        end += 1
        total += end

print(cnt)
