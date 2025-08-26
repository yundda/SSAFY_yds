T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())

    A = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        A[s].append(e)
        A[e].append(s)

    S, G = map(int, input().split())

    def BFS(S, G):
        isSuccess = False
        visited = [0] * (V + 1)
        visited[S] = 0
        Q = []
        Q.append(S)

        while Q:
            t = Q.pop(0)
            if t == G:
                isSuccess = True
                break
            for a in A[t]:
                if visited[a] == 0:
                    visited[a] = visited[t] + 1
                    Q.append(a)
        if not isSuccess:
            return 0
        else:
            return visited[G]

    ans = BFS(S, G)
    print(f"#{t} {ans}")
