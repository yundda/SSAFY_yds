import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    position_x= list(map(int,input().split()))
    position_y= list(map(int,input().split()))
    edges = []

    for i in range(N-1):
        for j in range(i+1,N):
            edges.append((i,j,(position_x[i] - position_x[j])**2 + (position_y[i] - position_y[j])**2))
    
    edges.sort(key=lambda x: x[2])

    E = float(input())
    linked = [i for i in range(N)]
    INF = 10**16
    cost = [INF] * N 

    def find(x):
        if x == linked[x]:
            return x
        linked[x] = find(linked[x])
        return linked[x]
    
    def union(a,b):
        x = find(a)
        y = find(b)
        if x != y:
            if x > y:
                linked[x] = y
            else:
                linked[y] = x
            return True
        return False
    
    cost[0] = 0
    cnt = min_cost = 0

    for start,end,cost in edges:
        if union(start,end):
            cnt += 1
            min_cost += cost
        if cnt == N-1:
            break

    min_cost *= E
    print(f'#{tc} {min_cost:.0f}')