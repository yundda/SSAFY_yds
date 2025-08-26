T = int(input())
for t in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    i = 1

    def inorder(node):
        global i
        if node > N:
            return
        # 왼쪽
        inorder(node * 2)
        # 현재 노드
        tree[node] = i
        i += 1
        # 오른쪽 노드
        inorder(node * 2 + 1)

    inorder(1)
    root = tree[1]
    child = tree[N // 2]

    print(f"#{t} {root} {child}")
