import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

n.sort()

def binary(x,s,e):
    mi = (s+e) // 2
    if s > e :
        print(0)
        return
    if(x > n[mi]):
        binary(x,mi+1,e)
    elif x < n[mi]:
        binary(x,s,mi-1)
    else:
        print(1)
        return

for x in m:
    binary(x,0,N-1)