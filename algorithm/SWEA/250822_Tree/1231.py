T = 1
for _ in range(T):
    N = int(input())

    li = [[] for _ in range(N+1)]
    for _ in range(N):
        A = list(input().split())

        node = int(A[0])
        li[node].append(A[1])

        l = int(A[2]) if len(A) > 2 else 0
        li[node].append(l)
        
        r = int(A[3]) if len(A) > 3 else 0
        li[node].append(r)
    

    def inorder(node):
        if node == 0:
            return
        inorder(li[node][1])

        print(li[node][0])
        
        inorder(li[node][2])

    inorder(1)