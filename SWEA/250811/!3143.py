T = int(input())
for t in range(1, T + 1):
    str1, str2 = map(list, input().split())
    N = len(str1)
    M = len(str2)

    i = 0
    cnt = 0
    while i < N:
        for p in range(M):
            if str1[i + p] != str2[p]:
                cnt += 1
                i += 1
                break
        else:
            cnt += 1
            i += M

    print(f"#{t} {cnt}")
