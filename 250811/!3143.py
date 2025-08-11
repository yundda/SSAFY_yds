T = int(input())
for t in range(1, T + 1):
    str1, str2 = input().split()
    str1 = list(str1)
    str2 = list(str2)

    N = len(str1)
    M = len(str2)

    cnt = 0
    i = 0
    while i < N - M + 1:
        for j in range(M):
            if str1[i + j] != str2[j]:
                i += 1
                break
        else:
            i += M
            cnt += 1

    result = N - (cnt * M) + cnt

    print(f"#{t} {result}")
