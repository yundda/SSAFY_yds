# 250806
T = 10
N = 100

for _ in range(T):
    t = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]

    def row_sum(arr):
        max_row_sum = 0
        for i in range(N):
            s = 0
            for j in range(N):
                s += arr[i][j]
            if max_row_sum < s:
                max_row_sum = s
        return max_row_sum

    def col_sum(arr):
        max_col_sum = 0
        for j in range(N):
            s = 0
            for i in range(N):
                s += arr[i][j]
            if max_col_sum < s:
                max_col_sum = s
        return max_col_sum

    def x_sum(arr):
        max_x_sum = 0
        s_r = 0
        s_l = 0
        for i in range(N):
            s_r += arr[i][i]
        for i in range(N):
            s_l += arr[i][N-1-i]
        return (s_r if s_r > s_l else s_l)

    max_val = max(row_sum(arr),col_sum(arr),x_sum(arr))
    
    print(f'#{t} {max_val}')
