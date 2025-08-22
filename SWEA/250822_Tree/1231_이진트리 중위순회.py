T = 1
for _ in range(T):

    N = int(input())
 
    tree = [[] for _ in range(N + 1)]
    for _ in range(N):
        arr = list(input().split())
        node = int(arr[0])
        c = arr[1]
        L = int(arr[2]) if len(arr) >=3 else 0
        R = int(arr[3]) if len(arr) >= 4 else 0

        tree[node].append(c)
        tree[node].append(L)
        tree[node].append(R)

    def inorder(node):
        global word
        if node == 0:
            return
        if node > N:
            return
        
        inorder(tree[node][1] )
        word += (tree[node][0])
        inorder(tree[node][2] )
    word = ''
    inorder(1)
    print(word)

# 8
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S
