import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited_rooms_line = [0] * 201

    for _ in range(N):
        x, y= map(int,input().split())
        s = min(x,y)
        e = max(x,y)
        start = (s+1) // 2
        end = (e+1) // 2
        for line in range(start,end+1):
            visited_rooms_line[line] += 1

    time = max(visited_rooms_line)
        
    print(f'#{tc} {time}')