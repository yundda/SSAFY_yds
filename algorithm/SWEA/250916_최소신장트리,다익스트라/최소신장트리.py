from heapq import heappop,heappush
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    edges = []
    parent = [i for i in range(V+1)]

    for i in range(E):
        s,e,w = map(int,input().split())
        edges.append((s,e,w))

    edges.sort(key=lambda x: x[2])

    def union(a,b):
        x = find(a)
        y = find(b)
        if x != y:
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
            return True
        return False

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]


    cnt = min_weight = 0
    for s,e,w in edges:
        if union(s,e):
            cnt += 1
            min_weight += w

        if cnt == V:
            break

    print(f'#{tc} {min_weight}')