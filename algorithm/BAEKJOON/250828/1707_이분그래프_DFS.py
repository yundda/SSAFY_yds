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

    def dfs(n,g):
        global isFail
        group[n] = g
        
        for con in A[n]:
            if group[con] == 0:
                dfs(con,-g)
            elif g * group[con] > 0 :
                isFail = True
                return
    
    for i in range(1,V+1):
        if group[i] == 0:
            dfs(i,1)
            if isFail:
                break
    

    if isFail:
        print("NO")
    else:
        print("YES")


