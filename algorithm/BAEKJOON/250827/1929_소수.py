N,M = map(int,input().split())
# A = [True]*(M + 1)
# A[0] = A[1] = False

# for i in range(2,M // 2 + 1):
#     for j in range(2, M // i + 1):
#             if i*j <= M:
#                 A[i*j] = False

# for i in range(N,M+1):
#     if A[i]:
#         print(i)


# for i in range(2,int(M**0.5) + 1):
#      if A[i]:
#           for j in range(i*i,M+1,i):
#                A[j] = False

# for i in range(N,M+1):
#     if A[i] and i != 1:
#         print(i)

A = [i for i in range(M+1)]
A[0] = A[1] = 0

for i in range(2, int(M**0.5)+1 ):
     if A[i] != 0:
          for j in range(i+i,M+1,i):
               A[j] = 0

for i in range(N,M+1):
     if A[i] != 0:
          print(i)