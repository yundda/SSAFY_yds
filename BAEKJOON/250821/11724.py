N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]


for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

stack = []
visited = [False] * (N + 1)
cnt = 0


def DFS(i):
    visited[i] = True
    stack.append(i)

    while stack:
        top = stack.pop()
        for a in A[top]:
            if not visited[a]:
                visited[a] = True
                stack.append(a)
    return


for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)


print(cnt)
