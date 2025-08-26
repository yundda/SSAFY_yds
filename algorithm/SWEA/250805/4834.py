# 250805
T = int(input())
for t in range(1, T +1):
    n = int(input())
    a = int(input())
    arr = [ 0 ] * 12
    while a > 0 :
        num = a % 10
        arr[num] += 1    
        a //= 10
    idx = 0
    max_num = 0
    for i in range(len(arr)-1, -1, -1):
        if max_num < arr[i]:
            max_num = arr[i]
            idx = i

    print(f'#{t} {arr}')