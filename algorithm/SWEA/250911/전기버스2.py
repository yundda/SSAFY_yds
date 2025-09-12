import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    N = A[0]
    M = A[1:]

    reach = M[0]
    pos = 0
    cnt = 0
    while reach < N-1:
        max_reach = 0
        for i in range(pos+1,reach+1):
            if max_reach <= M[i] + i: # 위치와 충전량 같이 더할 것!!! 
                max_reach = M[i] + i
                nxt_pos = i

        pos = nxt_pos
        reach = max_reach
        cnt += 1


    print(f'#{tc}', cnt)