print(1<<4)

arr = [1,3,5]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end = " ")
    print()



for i in range(1<<n): # i : 0 ~ 2^n -1 --> 2^n 번 시행 = n개 원소의 부분집합 개수
    for j in range(n): # 몇 번째 자리를 검사할지 -> 총 n 자리니까 range(n)
        if i & (1<<j): # i비트의 j번째 자리를 검사해서 1 있으면 True = i 가 j 번째 원소를 포함하고 있다 
            arr[j]