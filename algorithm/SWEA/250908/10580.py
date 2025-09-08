import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lines = [0]*N
    for i in range(N):
        s, e = map(int,input().split())
        lines[i] = (s,e)
    
    lines.sort()
    
    ans = 0
    for i in range(N - 1):
        s,e = lines[i]
        for j in range(i,N):
            if e > lines[j][1]:
                ans += 1

    print(f'#{tc} {ans}')