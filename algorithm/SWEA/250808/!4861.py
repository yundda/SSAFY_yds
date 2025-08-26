T = int(input())
for t in range(1, T + 1):
    N, M = (map(int,input().split()))
    arr = [list(input()) for _ in range(N)]

    def check(str_list,i):
        for p in range(int(M / 2)):
            if str_list[i+p] != str_list[i + M - 1 -p]: # (M-1)-(i+p) 로 착각했었음
                return False
        return True

    # 가로줄 확인
    def check_row(arr):
        isSuccess = False
        for string in arr:
            for i in range(N - M + 1):
                if check(string,i):
                    ans_list = [string[i+j] for j in range(M) ]
                    isSuccess = True                    
                    return ans_list
        if not isSuccess:
            return False

    # 세로줄 확인
    def check_col(arr):
        isSuccess = False
        for c in range(N):
            string = [arr[r][c] for r in range(N)]
            for i in range(N - M + 1):
                if check(string,i):
                    ans_list = [string[i+j] for j in range(M) ]
                    isSuccess = True
                    return ans_list
        if not isSuccess:
            return False

    check_col(arr)
    if check_row(arr):
        ans_list = check_row(arr)
    else:
        ans_list = check_col(arr)
    
    print(f'#{t}',''.join(ans_list))
        