#### 인접 리스트 ####
N = 6
V = 7
A = [[0] * (V + 1) for _ in range(V + 1)]
visited = [0] * (V + 1)

for _ in range(N):
    a, b = map(int, input().split())
    A[a][b] = 1
    A[b][a] = 1


def DFS(s):
    visited[s] = 1
    stack = [s]

    while stack:
        cur = stack.pop()
        print("pop ->", cur, "stack:", stack)
        for n in range(1, V + 1):
            if A[cur][n] == 1 and not visited[n]:
                visited[n] = 1
                stack.append(n)


DFS(1)


##### 인접 행렬 ####
N = 6
V = 7
A = [[] for _ in range(V + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    A[a].append(b)

visited = [0] * (V + 1)


def DFS(S):
    stack = []

    visited[S] = 1
    stack.append(S)

    while stack:
        cur = stack.pop()
        print(cur, stack)

        for n in A[cur]:
            if visited[n] != 1:
                visited[n] = 1
                stack.append(n)


DFS(1)
