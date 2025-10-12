import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    paper = list(map(int,input().split()))
    represent = [i for i in range(N+1)]

    def union(a,b):
        x = find(a)
        y = find(b)
        if x < y:
            represent[y] = x
        elif x > y:
            represent[x] = y


    def find(x):
        if x == represent[x]:
            return x
        
        represent[x] = find(represent[x])
        return represent[x]

    for i in range(M):
        union(paper[2*i],paper[2*i+1])

    
    for i in range(1, N+1):
        represent[i] = find(i)

    cnt = 0
    for i in range(1,N+1):
        if represent[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')