A = [7,4,3,9,1,4,6,5,8]

N = len(A)
# def quick(start, end):
#     if start>=end:
#         return
#     pivot = A[start]
#     i = start+1
#     j = end
#     while i <= j:
#         while i <= end and A[i] <= pivot:
#             i += 1
#         while j >= start and A[j] > pivot:
#             j -= 1
#         if i < j:
#             A[i], A[j]= A[j], A[i]
#             i += 1
#             j -= 1
    
#     A[j], A[start] = A[start], A[j]
#     quick(start,j-1)
#     quick(j+1,end)

# quick(0,N-1)
# print(A)
    
    

def quick(start, end):
    if start < end:
        pivot = A[start]
        i , j = start+1, end

        while i <= j:
            while i <= end and A[i] <= pivot:
                i += 1
            while j > start and A[j] > pivot:
                j -= 1
            if i < j:
                A[i],A[j] = A[j],A[i]
                i += 1
                j -= 1
        
        A[j], A[start] = A[start], A[j]
        quick(start, j-1)
        quick(j+1, end)

quick(0,N-1)
print(A)