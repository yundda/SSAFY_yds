T = int(input())
for t in range(1, T +1):
    N, K = (map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]

    def check_three(a,i):
        for p in range(K-1):
            if a[i+p+1] == 0:
                return False
        return True

    def check_row(a):
        cnt = 0
        for i in range(N-K+1):
            isFail = False
            # print(a[i])
            if a[i] == 1:
                if check_three(a,i):      
                    if (i == 0 or a[i-1] == 0) and (i == N-K or a[i+K] == 0):
                        cnt += 1
        return cnt    

    cnt = 0
    for row in arr:
        cnt += check_row(row)
    
    # for j in range(N):
    #     col_arr = [0]*N
    #     for i in range(N):
    #         col_arr[i] = arr[i][j]
    #     cnt += check_row(col_arr)

    for j in range(N):
        col_arr = [arr[i][j] for i in range(N)]
        cnt += check_row(col_arr)

    print(f'#{t} {cnt}')