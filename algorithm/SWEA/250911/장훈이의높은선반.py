import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    heights.sort(reverse = True)
    used = [False] * N
    over = []


    min_sum = 10**10
    def recur(now,sum_heights):
        global min_sum

        if sum_heights == B:
            return True

        if sum_heights > B and min_sum > sum_heights:
            min_sum = sum_heights
            return False

        if now == N-1:
            return False
        
        for i in range(now+1,N):

            used[i] = True
            if recur(i,sum_heights+heights[i]):
                return True
            used[i] = False

        return False


     
    if recur(-1,0):
        ans = 0
    else:
        ans = min_sum - B
    
    print(f'#{tc} {ans}')