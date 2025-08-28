### 그리디 알고리즘으로 풀 수 있는 이유 = A가 배수로 이루어져있기 때문!!!그렇지 않으면 반례 발생

N, K = map(int,input().split())
A = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1,-1,-1):
    if K >= A[i]:
        cnt += K // A[i]
        K %= A[i]


# while문 사용 필요 없음
# while K != 0:
#     for i in range(N-1,-1,-1):
#         if K >= A[i]:
#             a = A[i]
#             break
#     cnt += K // a
#     K %= a

print(cnt)