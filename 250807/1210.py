import copy

for _ in range(10):
    t = int(input())
    a = [list(map(int,input().split())) for _ in range(N)]
    N = 100

    # 오(R), 왼(L), 아(D)
    dr = [0, 0, 1]
    dc = [1, -1, 0]

    def find_dir(A,r,c):
        for i in range(3):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if in_range(next_r, next_c) and A[next_r][next_c] >= 1:
                return next_r,next_c

    def in_range(r,c):
        return r >= 0 and r < N and c >=0 and c < N

    isSuccess = False
    ans = 0
    for i in range(N):
        r = 0
        c = i
        if a[r][c] == 1:
            A = copy.deepcopy(a)
            while True:
                if r == N -1:
                    break
                next_r,next_c = find_dir(A,r,c)
                if r == next_r and c == next_c:
                    break
                r = next_r
                c = next_c
                if A[r][c] == 2 :
                    isSuccess = True
                    break
                A[r][c] = -1
            if isSuccess:
                ans = i
                break
    print(f'#{t} {ans}')
