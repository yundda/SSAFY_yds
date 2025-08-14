T = int(input())
for t in range(1, T + 1):
    N, min_cnt, max_cnt = map(int, input().split())

    scores = list(map(int, input().split()))

    count = [0] * 101

    for i in range(N):
        s = scores[i]
        count[s] += 1

    for i in range(1, N + 1):
        count[i] += count[i - 1]

    sorted_scores = [0] * N
    cnt = count.copy()
    for i in range(N):
        s = scores[i]
        cnt[s] -= 1
        sorted_scores[cnt[s]] = s

    min_val = 1000
    for i in range(N - 1):
        c1 = count[sorted_scores[i]]
        if min_cnt <= c1 <= max_cnt:
            for j in range(i + 1, N):
                c2 = count[sorted_scores[j]] - c1
                if min_cnt <= c2 <= max_cnt:
                    for z in range(j + 1, N):
                        c3 = N - (c1 + c2)
                        if min_cnt <= c3 <= max_cnt:
                            student = sorted([c1, c2, c3])
                            dif = student[2] - student[0]
                            if min_val > dif:
                                min_val = dif

    ans = min_val if min_val != 1000 else -1

    print(f"#{t} {ans}")
