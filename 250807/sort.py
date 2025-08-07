# # 선택 정렬 내림차순
A = [2,4,3,6,1,7,4,3,9]
N = len(A)

for i in range(N-1):
    max_idx = i
    for j in range(i+1,N):
        if A[max_idx] < A[j]:
            max_idx = j
    A[max_idx], A[i] = A[i], A[max_idx]

print(A)

# # 선택 정렬 K번째 큰 수 구하기
A = [2,4,3,6,1,7,4,3,9]
N = len(A)
K = 6
for i in range(K):
    max_idx = i
    for j in range(i + 1, N):
        if A[max_idx] < A[j]:
            max_idx = j
    A[max_idx], A[i] = A[i], A[max_idx]

print(A[K-1])

# # 버블 정렬 오름 차순
A = [2,4,3,6,1,7,4,3,9]
N = len(A)
for i in range(N-1, -1,-1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
print(A)

# # 카운트 정렬
A = [2,4,3,6,1,7,4,3,9]
N = len(A)
count = [0] * 10

for i in range(N):
    count[A[i]] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

arr = [0] * len(A)

for i in range(len(A)):
    num = A[i]
    count[num] -= 1
    arr[count[num]] = num

print(arr)