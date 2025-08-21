#### 슬라이딩 윈도우 ####
S, P = map(int, input().split())
str = list(input())
p_cnt = list(map(int, input().split()))

must = {
    "A": p_cnt[0],
    "C": p_cnt[1],
    "G": p_cnt[2],
    "T": p_cnt[3],
}

p_dic = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0,
}


def in_range(p_dic):
    for k in "ACGT":
        if p_dic[k] < must[k]:
            return False
    return True


for i in range(P):
    p_dic[str[i]] += 1

cnt = 0
start = 0
end = P - 1
while True:
    if in_range(p_dic):
        cnt += 1
    p_dic[str[start]] -= 1
    start += 1

    end += 1
    if end == S:
        break
    p_dic[str[end]] += 1

print(cnt)


#### 슬라이딩 윈도우 ####
S, P = map(int, input().split())
str = list(input())
p_cnt = list(map(int, input().split()))

must = {
    "A": p_cnt[0],
    "C": p_cnt[1],
    "G": p_cnt[2],
    "T": p_cnt[3],
}


def in_range(idx):
    p_dic = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    for i in range(idx, P + idx):
        p_dic[str[i]] += 1
    for k in "ACGT":
        if p_dic[k] < must[k]:
            return False
    return True


cnt = 0

for i in range(S - P + 1):
    if in_range(i):
        cnt += 1

print(cnt)
