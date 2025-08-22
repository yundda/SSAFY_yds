T = 1
for _ in range(T):

    N = int(input())
    # k = 0

    # def find_k(N):
    #     global k
    #     if N == 1:
    #         return
    #     k += 1
    #     find_k(N // 2)

    # find_k(N)
    # for i in range(k):
    #     for j in range(2**i):
    #         node, c, L, R = (input().split())
    #         node = int(node)
    #         if L:
    #             L = int(L)
    #         if R:
    #             R = int(R)
    tree = [[] for _ in range(N)]
    for _ in range(N):
        arr = list(input().split())

        if len(arr) == 4:
            node, c, L, R = int(arr[0]), arr[1], int(arr[2]), int(arr[3])
        elif len(arr) == 3:
            node, c, L, R = int(arr[0]), arr[1], int(arr[2]), 0
        else:
            node, c, L, R = int(arr[0]), arr[1], 0, 0

        print(node, c, L, R)
