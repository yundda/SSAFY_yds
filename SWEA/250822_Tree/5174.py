T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]
    for i in range(E):
        tree[arr[i * 2]].append(arr[i * 2 + 1])

    c = tree[N]

    sub_node = 0

    def DFS(S):
        global sub_node
        sub_node += 1
        global max_edge
        if not tree[S]:
            return
        for child in tree[S]:
            DFS(child)

    DFS(N)

    print(f"#{t} {sub_node}")
