T = int(input())
for t in range(1,T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    H = [0] * (N+1)

    def push(x,last):
        H[last] = x
        p = last // 2
        c = last
        while p > 0 and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2

    def sum_par(last):
        sum = 0
        p = last // 2
        while p > 0:
            sum += H[p]
            p //= 2
        return sum


    for i,a in enumerate(A):
        push(a,i+1)
    
    ans = sum_par(N)


    print(f'#{t} {ans}')


'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''
