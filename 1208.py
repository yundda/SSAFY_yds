# 250805
T = 10
for t in range(1,T+1):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))

    def dump(box_list):
        global isFinish
        h_box = 1
        l_box = 100
        h_idx, l_idx = 0, 0

        for idx, box in enumerate(box_list):
            if h_box < box:
                h_box = box
                h_idx = idx
            if l_box > box:
                l_box = box
                l_idx = idx
        if h_box - l_box <= 1:
            isFinish = True
            return box_list

        box_list[h_idx] -= 1
        box_list[l_idx] += 1
        print(box_list)
        return box_list

    isFinish = False
    for _ in range(dump_cnt):
        if isFinish:
            break
        box_list = dump(box_list)

    ans = max(box_list) - min(box_list)

    print(f'#{t} {ans}')