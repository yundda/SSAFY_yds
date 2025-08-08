T = int(input())
for t in range(1, T+1):
    s1 = list(input())
    s2 = list(input())

    max_cnt = 0
    for s in s1:
        cnt = 0
        for i in range(len(s2)):
            if s == s2[i]:
                cnt += 1
        if max_cnt < cnt :
            max_cnt = cnt


    print(f'#{t} {max_cnt}')