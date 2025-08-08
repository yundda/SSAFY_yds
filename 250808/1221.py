T = int(input())
for _ in range(T):
    t, N = (input().split())
    str_num = list(input().split())
    N = int(N)

    dic = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9
    }

    def sort_str(arr):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1,N):
                if dic[arr[min_idx]] > dic[arr[j]]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr

    ans = sort_str(str_num)

    print(t)
    print(*ans)
        