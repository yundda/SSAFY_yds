T = int(input())
for _ in range(T):
    N, M = (map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]

    dr = [0,1,0,-1,-1,1,1,-1]
    dc = [1,0,-1,0,1,1,-1,-1]

    def in_range(r,c):
        return 0 <= r < N and 0 <= c < N
    
    def kill(i,j):
        s1 = 0
        s2 = 0
        for idx in range(8):
            for m in range(1, M ):
                next_r = i + dr[idx] * m
                next_c = j + dc[idx] * m
                if in_range(next_r,next_c):
                    if idx < 4 :
                        s1 += arr[next_r][next_c]
                    else:
                        s2 += arr[next_r][next_c]
        # print(s1,s2)
        max_kill = s1 if s1 > s2 else s2
        max_kill += arr[i][j]
        return max_kill

    max_val = 0
    for i in range(N):
        for j in range(N):
            if max_val < kill(i,j):
                max_val = kill(i,j)

    print(max_val)


