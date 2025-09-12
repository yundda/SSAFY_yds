A = [7,4,3,9,1,4,6,5,8]

# def partition(left, right):
#     if left < right:
#         mid = (left + right) // 2
#         partition(left,mid)
#         partition(mid+1,right)
#         merge(left,mid,right)

# def merge(start,mid,end):
#     L = A[start:mid+1]
#     R = A[mid+1:end+1]
#     l = len(L)
#     r = len(R)

#     i = j = 0
#     k = start

#     while i < l and j < r:
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#             k += 1
#         else:
#             A[k] = R[j]
#             j += 1
#             k += 1

#     while i < l:
#         A[k] = L[i]
#         i += 1
#         k += 1

#     while j < r:
#         A[k] = R[j]
#         j += 1
#         k += 1

# partition(0,len(A)-1)
# print(A)



def merge(start,mid,end):
    L = A[start:mid+1]
    R = A[mid+1:end+1]
    l = len(L)
    r = len(R)

    i = j = 0
    k = start
    while i < l and j < r:
        if L[i] > R[j]:
            A[k] = L[i]
            i += 1
            k += 1

        else:
            A[k] = R[j]
            j += 1
            k += 1
    
    while j < r:
        A[k] = R[j]
        j += 1
        k += 1

    while i < l:
        A[k] = L[i]
        i += 1
        k += 1



def partition(left,right):
    if left < right:
        mid = (left + right) // 2
        partition(left,mid)
        partition(mid+1,right)
        merge(left,mid,right)

    
partition(0,len(A)-1)
print(A)