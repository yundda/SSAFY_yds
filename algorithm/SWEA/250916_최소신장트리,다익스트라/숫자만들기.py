import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    max_val = -10**10
    min_val = 10**10


    def calc(val,idx):
        global max_val, min_val

        if idx == N:
            max_val = max(max_val,val)
            min_val = min(min_val,val)
            return

        for i in range(4):
            if op[i] <= 0:
                continue
            if i == 0:
                new_val = val + numbers[idx]
            elif i == 1:
                new_val = val - numbers[idx]
            elif i == 2:
                new_val = val * numbers[idx]
            elif i == 3:
                new_val = int(val / numbers[idx])

            op[i] -= 1
            calc(new_val,idx+1)
            op[i] += 1

    calc(numbers[0],1)

    ans = max_val - min_val
    print(f'#{tc} {ans}')