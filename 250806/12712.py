T = int(input())
for t in range(1, T + 1):
    N, M = (map(int,input().split()))
    arr = [ list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 1, -1, 0, 1, 0, -1]
    dc = [1, 1, -1, -1, 1, 0, -1, 0]

    def in_range(r,c):
        return r >= 0 and r < N and c >= 0 and c < N

    def plus_kill(i,j):
        kill = 0
        for p in range(4,8):
            for l in range(1,M):
                r = i + dr[p]*l
                c = j + dc[p]*l
                if not in_range(r,c):
                    continue
                kill += arr[r][c]
        kill += arr[i][j]
        return kill

    def x_kill(i, j):
        kill = 0
        for p in range(4):
            for l in range(1,M):
                r = i + dr[p]*l
                c = j + dc[p]*l
                if not in_range(r,c):
                    continue
                kill += arr[r][c]
        kill += arr[i][j]
        return kill



    def kill(i, j):
        x_kill = 0
        plus_kill = 0
        for p in range(8):
            for l in range(1,M):
                r = i + dr[p]*l
                c = j + dc[p]*l
                if not in_range(r,c):
                    continue
                if p < 4:
                    plus_kill += arr[r][c]
                else :
                    x_kill += arr[r][c]
        kill = plus_kill if plus_kill > x_kill else x_kill
        kill += arr[i][j]
        return kill





    # max_kill = 0
    # for i in range(N):
    #     for j in range(N):
    #         kill = plus_kill(i,j) if plus_kill(i,j) > x_kill(i,j) else x_kill(i,j)
    #         if max_kill < kill:
    #             max_kill = kill

    max_kill = 0
    for i in range(N):
        for j in range(N):
            killed = kill(i,j)
            if max_kill < killed:
                max_kill = killed
    


    
    print(f'#{t} {max_kill}')
