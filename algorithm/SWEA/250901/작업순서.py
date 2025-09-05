from collections import deque
import sys
sys.stdin = open('input.txt','r')
T = 10
for t in range(1,T+1):
    V, E = map(int,(input().split()))
    A = list(map(int,input().split()))

    pre = [[] for _ in range(V+1)]
    C = [0] * (V+1)
    for i in range(E):
        s = A[2*i]
        e = A[2*i+1]
        pre[s].append(e)
        C[e] += 1

    q = deque()

    for i in range(1,V+1):
        if C[i] == 0:
            q.append(i)

    print(f'#{t}', end = " ")
    while q:
        now = q.popleft()
        print(now, end = " ")
        for con in pre[now]:
            C[con] -= 1
            if C[con] == 0:
                q.append(con)
    print()



