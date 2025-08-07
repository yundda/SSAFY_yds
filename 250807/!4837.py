T = int(input())
for t in range(1, T +1):
    N, K = (map(int,input().split()))
    num = 12
    A = [i for i in range(1,num+1)]

    ans = 0
    for i in range(1<<num):
        s, cnt = 0, 0
        for j in range(num):
            if i & (1<<j):
                s += A[j]
                cnt += 1
        if s == K and cnt == N:
            ans += 1
    print(f'#{t} {ans}')
