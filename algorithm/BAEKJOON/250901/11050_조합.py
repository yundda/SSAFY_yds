import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int,input().split())

# comb = [[0]*(N+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     for j in range(+1):
#         if j == 0 or j == i:
#             comb[i][j] = 1
#         elif j == 1 or j == i-1:
#             comb[i][j] = i
#         else:
#             comb[i][j] = comb[i-1][j-1] + comb[i-1][j]


A = [[-1]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    A[i][0] = 1
    A[i][i] = 1
    A[i][1] = i

def comb(n,r):
    if A[n][r] == -1:
        A[n][r] = comb(n-1,r-1)+comb(n-1,r)
    return A[n][r]

ans = comb(N,K)
# ans = comb[N][K]
print(ans)