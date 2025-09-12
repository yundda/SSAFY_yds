import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    cnt = 0
    def recur(n,sum_val):
        global cnt
        if sum_val == K:
            cnt += 1
            return

        if n == N:
            return
    
        # for i in range(n+1,N):
        #     recur(i,sum_val + A[i])
        recur(i+1,sum_val + A[i])
        recur(i+1,sum_val)

    
    recur(-1,0)

    print(f'#{tc} {cnt}')