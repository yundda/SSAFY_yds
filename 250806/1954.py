# 250806
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    def is_in_range(r,c):
        return r >= 0 and r < N and c >= 0 and c < N

    # 오 -> 아 -> 왼 -> 위
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    r, c, direction = 0, 0, 0
    arr[0][0] = 1
    cnt = 1
    while cnt != N * N:
        next_r = r + dr[direction]
        next_c = c + dc[direction]

        if not is_in_range(next_r,next_c) or arr[next_r][next_c] != 0:
            direction = (direction + 1) % 4
            continue
        
        r = next_r
        c = next_c
        cnt += 1
        arr[r][c] = cnt

    
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()