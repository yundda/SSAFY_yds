import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N // 2
    S = [list(map(int,input().split())) for _ in range(N)]
    min_val = 10**10

    def synergy(ingre):
        s = 0
        for i in range(n-1):
            for j in range(i+1,n):
                s += S[ingre[i]][ingre[j]] + S[ingre[j]][ingre[i]]
        return s

    for i in range(1<<N):
        cnt = 0
        ingre_a = []
        ingre_b = []
        for idx in range(N):
            if i & (1<<idx):
                ingre_a.append(idx)
                cnt += 1
        if cnt == n:
            A = synergy(ingre_a)
            for i in range(N):
                if i in ingre_a:
                    continue
                ingre_b.append(i)
            B = synergy(ingre_b)
            val = abs(A - B)
            if min_val > val:
                min_val = val

    print(f'#{tc} {min_val}')