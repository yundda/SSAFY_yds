import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

visited = [False] * (N + 1)

def tracking(node):
    visited[node] = True

    if len(A[node]) == 0:
        return

    for n in A[node]:
        if not visited[n]:
            tracking(n)


cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        tracking(i)
        cnt += 1

print(cnt)