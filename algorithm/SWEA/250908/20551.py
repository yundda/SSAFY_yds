import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    a, b, c = map(int,input().split())

    ans = 0
    isFail = False
    if b >= c:
        past = b
        b = c-1
        ans += (past - b)

    if a >= b:
        past = a
        a = b-1
        ans += (past - a)

    if a < 1 or b < 1 or c < 1:
        isFail = True

    ans = ans if not isFail else -1
    print(f'#{tc} {ans}')