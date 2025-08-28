import sys
sys.setrecursionlimit(10**6)
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
    isFail = False
    visited = [False] * (V+1)
    
    def dfs(n,g):
        visited[n] = True
        group[n] = g

        for con in A[n]:
            if not visited[con]:
                if not dfs(con,-g):
                    return False
            else:
                if group[con] == group[n]:
                    return False
        return True
    
    for i in range(1,V+1):
        if group[i] == 0:
            if not dfs(i,1):
                isFail = True
                break
    

    if isFail:
        print("NO")
    else:
        print("YES")
