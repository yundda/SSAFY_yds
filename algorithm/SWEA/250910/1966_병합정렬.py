import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    def merge(left,mid,right):
        L = A[left:mid+1]
        R = A[mid+1:right+1]
        l = len(L)
        r = len(R)

        i = j = 0
        k = left

        while i < l and j < r:
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
                k += 1
            else:
                A[k] = R[j]
                j += 1
                k += 1

        while i < l:
            A[k] = L[i]
            i += 1
            k += 1

        while j < r:
            A[k] = R[j]
            j += 1
            k += 1


    def partition(left, right):
        if left == right:
            return
        
        mid = (left+right) // 2
        partition(left,mid)
        partition(mid+1,right)
        merge(left,mid,right)

    partition(0,N-1)
    print(f'#{tc}', *A)