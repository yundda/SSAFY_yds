import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

max_cnt = 2

cnt = 1
for i in range(N-1):
    if A[i] >= A[i+1]:
        cnt+=1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
        
cnt = 1
for i in range(N-1):
    if A[i] <= A[i+1]:
        cnt+=1
    else:
        cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

if N == 1:
    max_cnt = 1

print(max_cnt)