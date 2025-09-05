import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1,T+1):
    M, K = input().split()
    M = list(M)
    max_M = max(M)
    K = int(K)
    max_value = 0
    def money(n):
        global max_value

        if n == K:
            s = int(''.join(M))

            if max_value < s:
                max_value = s    
            return
        
        for i in range(len(M)-1):
            for j in range(i+1,len(M)):
                if int(M[i]) > int(M[j]) and i < len(M)-2 :
                    continue
                M[i],M[j] = M[j],M[i]
                if M[0] == max_M:
                    money(n+1)
                M[i],M[j] = M[j],M[i]

    if len(M) == 1:
        print(f'#{t} {int(M[0])}')
    elif len(M) == 2:
        if K % 2 == 1:
            ans = int(''.join(M[::-1]))
        else:
            ans = int(''.join(M))
        print(f'#{t} {ans}')
    else:
        money(0)
        print(f'#{t} {max_value}')