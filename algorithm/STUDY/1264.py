import sys
sys.stdin = open('input.txt','r')

while True:
    cnt = 0
    A = list(input())
    if A == ['#']:
        break
    
    for a in A:
        if a in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
