n = int(input())
D = [0]*(n+1)

D[1] = 1
if n >=2:
    D[2] = 2


for i in range(3,n+1):
    D[i] = D[i-1] + D[i-2]

print(D[n] % 10007)


def dp(i):
    if D[i] == 0:
        D[i] = dp(i-1) + dp(i-2)
    return D[i]

print(dp(n) % 10007)