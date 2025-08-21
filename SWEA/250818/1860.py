T = int(input())
for t in range(1,T+1):
    N,M,K = (map(int,input().split()))
    MAX_T = 11112
    A = list(map(int,input().split()))
    A.sort()

    result = 'Possible'
    for i in range(len(A)):
        made = (A[i]//M) * K
        if i+1 > made:
            result = 'Impossible'
            
    
    print(f'#{t} {result}')
