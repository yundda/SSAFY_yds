T = int(input())
for t in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    N = len(str1)
    M = len(str2)

    result = 0

    for i in range(M - N + 1):
        isSuccess = True
        for k in range(N):
            if str2[i + k] != str1[k]:
                isSuccess = False
            if not isSuccess:
                break
        if isSuccess:
            result = 1
            break

    print(f"#{t} {result}")
