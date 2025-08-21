T = int(input())
for t in range(1, T +1):
    N = int(input())
    A = list(map(int,input().split()))
    

    for i in range(N-1):
        if i % 2 != 0:
            max_idx = i
            for j in range(i+1, N):
                if A[max_idx] > A[j]:
                    max_idx = j
            A[i], A[max_idx] = A[max_idx], A[i]
        else:
            min_idx = i
            for j in range(i+1, N):
                if A[min_idx] < A[j]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]

    print(f'#{t} ')
    for i in range(10):
        print(A[i], end = " ")
    print()
