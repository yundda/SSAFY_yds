T = int(input())
for t in range(1, T + 1):
    N, M = (map(int,input().split()))
    arr = [ list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = 0
            for p in range(M):
                for q in range(M):
                    kill += arr[i + p][j + q]
            if max_kill < kill:
                max_kill = kill


    
    print(f'#{t} {max_kill}')