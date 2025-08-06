## 250804

arr = [0, 0,254, 185, 76, 227, 84, 175, 0, 0]
N = 10
ans = 0
for i in range(2, N-2):
    max_f = 0
    for j in range(i-2, i+3):
        if j != i:
            # print(arr[j])
            if max_f < arr[j]:
                max_f = arr[j]
    # print(arr[i], max_f)
    cnt = 0
    view = arr[i] - max_f if arr[i] - max_f > 0 else 0
    # print(view)
    ans += view

print(ans)

list(map(int, input().split()))