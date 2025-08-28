import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int,input().split())
    A = [[] for _ in range (V+1)]
    
    for _ in range(E):
        u, v = map(int,input().split())
        A[u].append(v)
        A[v].append(u)
    
    group = [0] * (V+1)
    q = deque()    

    def bfs(node):
        q.append(node)
        group[node] = 1

        while q:
            now = q.popleft()
            for nxt in A[now]:
                if group[nxt] == 0:
                    group[nxt] = -group[now]
                    q.append(nxt)
                else:
                    if group[now] == group[nxt]:
                        return False
        return True


    for i in range(1,V+1):
        if group[i] == 0:
            if not bfs(i):
                print("NO")
                break
    else : print("YES")
