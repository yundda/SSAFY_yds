T = int(input())
for t in range(1,T + 1):
    N,M,L = map(int, input().split())
    
    tree = [0] * (N+1)
    
    for _ in range(M):
        n, x = map(int, input().split())
        tree[n] = x
        p = n //2
        while p > 0:
            tree[p] += x
            p //= 2
    
    ans = tree[L]

    print(f'#{t} {ans}')

'''
1
10 5 2
8 42
9 468
10 335
6 501
7 170
'''