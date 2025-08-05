# 250805
T = int(input())
for t in range(1, T + 1):
    K, N, M = (map(int, input().split()))
    Machine = list(map(int, input().split()))
    total = [0] * (N + 1)
    cnt = 0
    pos = 0
    isFail = False
    while True:
        if pos + K >= N or cnt >= M:
            break
        for i in range(M-1, -1, -1):
            if pos + K >= Machine[i]:
                if pos == Machine[i]:
                    isFail = True
                    break
                pos = Machine[i]
                total[Machine[i]] = 1
                cnt += 1
                break
        if isFail:
            cnt = 0
            break      
    print(f'{t} {cnt}')
