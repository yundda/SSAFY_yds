T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))

    def is_aec(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    max_val = -1
    for i in range(N-1):
        for j in range(i+1, N):
            a = A[i] * A[j]
            arr = list(str(a))
            if is_aec(arr):
                if max_val < a:
                    max_val = a
            
    print(f'#{t} {max_val}')
