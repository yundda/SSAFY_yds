import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
    visited = [0] * 201
    for i in range(N):
        r1,r2 = map(int,input().split())
        start = min(r1,r2)
        end = max(r1,r2)
        s =  (start + 1) // 2
        e = (end + 1) // 2
        for j in range(s,e+1):
            visited[j] += 1


    ####### !!!!! max로 겹치는 최대 구간 찾기!!!!!! #####
    time = max(visited)
        
    print(f'#{tc} {time}')