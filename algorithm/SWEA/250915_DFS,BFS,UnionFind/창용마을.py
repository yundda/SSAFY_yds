from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())

    represent = [i for i in range(N+1)]

    def union(a,b):
        x = find(a)
        y = find(b)
        if x != y:
            if x > y:
                represent[x] = y
            else:
                represent[y] = x

    def find(x):
        if x == represent[x]:
            return x
        represent[x] = find(represent[x])
        return represent[x]

    for _ in range(M):
        a,b = map(int,input().split())
        union(a,b)

    for i in range(1,N+1):
        find(i)

    cnt = 0
    for i in range(1,N+1):
        if i == represent[i]:
            cnt += 1



    print(f'#{tc} {cnt}')