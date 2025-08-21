T = int(input())
for t in range(1, T +1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    # min_idx = 0
    for i in range(N-1):
        min_idx = i     # 최소 값은 i 로 초기화!!
        for j in range(i+1,N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f'#{t}',*arr)