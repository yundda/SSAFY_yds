A = [0,1,2,3,1,4,5]

def union(s,b):
    A[b] = find(s)

def find(n):
    if A[n] == n:
        return n
    val = find(A[n])
    return val

union(4,6)