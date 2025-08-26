T = int(input())
for t in range(1, T +1):
    P, A, B = (map(int,input().split()))
    def find_page(P,F):
        s = 1
        f = P
        cnt = 0
        c = int((f+s) / 2)
        while c != F:            
            if s < F < c :
                f = c
            elif F > c :
                s = c
            c = int((f+s) /2)
            cnt += 1
        return cnt 
    a = find_page(P,A)
    b = find_page(P,B)
    if a < b:
        result = 'A'
    elif a > b:
        result = 'B'
    else:
        result = 0
    
    print(f'#{t} {result}')
