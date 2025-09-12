import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = list(map(int,input().split()))
    address = [0] * (N+2)
    visited = [False] * (N+2)
    
    for i in range(N+2):
        address[i] = (V[2*i],V[2*i+1])

    min_distance = 10**10
    def recur(now_idx,cnt,total_distance):
        global min_distance
        if cnt == N:
            home_x, home_y = address[1]
            now_x,now_y = address[now_idx]
            total_distance += (abs(now_x - home_x) + abs(now_y - home_y))
            if min_distance > total_distance:
                min_distance = total_distance
            return

        for idx in range(2,N+2):
            if visited[idx]:
                continue
            now_x,now_y = address[now_idx]
            nxt_x,nxt_y = address[idx]

            distance = abs(now_x - nxt_x) + abs(now_y - nxt_y)
            # 거리 가지치기
            if min_distance < total_distance + distance:
                continue
            visited[idx] = True
            recur(idx,cnt+1,total_distance+distance)
            visited[idx] = False

    
    recur(0,0,0)

    print(f'#{tc} {min_distance}')



#1 200
#2 304
#3 265
#4 307
#5 306
#6 366
#7 256
#8 399
#9 343
#10 391