import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    def sliding(A,B):
        max_val = 0
        for i in range(len(B)-len(A)+1):
            value = 0
            for j in range(len(A)):
                value += A[j]*B[i+j]
            if max_val < value:
                max_val = value
        return max_val


    if len(A) > len(B):
        max_value = sliding(B,A)
    else:
        max_value = sliding(A,B)

    print(f'#{tc} {max_value}')