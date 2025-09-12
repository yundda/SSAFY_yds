import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    def quick(left, right):
        if left >= right:
            return
        i, j = left, right
        m = (left+right) // 2
        pivot = A[m]

        while i <= j :
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j :
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        A[j], A[m] = A[m], A[j]
        quick(left, j-1)
        quick(j+1,right)

    quick(0,N-1)
    print(f'#{tc}', *A)