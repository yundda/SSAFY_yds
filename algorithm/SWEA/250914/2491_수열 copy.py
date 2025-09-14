import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

max_cnt = 2
def acs_cnt(i,cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    if i == N-1:
        return
    
    if A[i] > A[i+1]:
        acs_cnt(i+1,1)
    else:
        acs_cnt(i+1,cnt+1)


def desc_cnt(i,cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    
    if i == N-1:
        return
    
    if A[i] < A[i+1]:
        desc_cnt(i+1,1)
    else:
        desc_cnt(i+1,cnt+1)
if N > 1:
    acs_cnt(0,1)
    desc_cnt(0,1)
else:
    max_cnt = 1
print(max_cnt)