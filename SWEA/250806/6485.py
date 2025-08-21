T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] * 5001
    for _ in range(N):
        a, b = (map(int, input().split()))
        for i in range(a,b+1):
            arr[i] += 1

    P = int(input())
    c = list(int(input()) for _ in range(P))
    result = [0] * P
    for i in range(0, P):
        result[i] = arr[c[i]]
    
    print(f'#{t}', end = " ")
    print(*result)