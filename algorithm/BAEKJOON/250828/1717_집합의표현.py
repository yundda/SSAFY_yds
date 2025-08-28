import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
A = [i for i in range(n+1) ]

def find(x):
    if A[x] == x:
        return x
    A[x] = find(A[x])
    return A[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            A[a] = b
        else:
            A[b] = a 

def prt(a,b):
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")

for _ in range(m):
    z, a, b = map(int,input().split())
    if z == 1:
        prt(a,b)
    else:
        union(a,b)
