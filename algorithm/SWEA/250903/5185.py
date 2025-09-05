T = int(input())
for t in range(1,T+1):
    d = {
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15
    }

    def chgX(x):
        if x in 'ABCDEF':
            x = d[x]
        else:
            x = int(x)

        a = []
        for _ in range(4):
            a.append(x % 2)
            x //= 2
        return a[::-1]
    
    N,X = input().split()
    N = int(N)
    ans = [] 

    for x in X:
        ans.extend(chgX(x))
    
    print(f'#{t}', end = " ")
    for a in ans:
        print(a, end="")
    print()


