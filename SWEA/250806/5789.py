T = int(input())
for t in range(1, T+1):
    N, Q = (map(int,input().split()))
    A = [0] * N
    for i in range(1,Q+1):
        L, R = (map(int,input().split()))
        for x in range(L-1,R):
            A[x] = i
    print(f'#{t}', end = " ")
    print(A)