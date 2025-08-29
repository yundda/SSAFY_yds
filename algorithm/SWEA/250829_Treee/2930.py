import heapq
T = int(input())
for t in range(1,T+1):
    N = int(input())
    ans = []
    q = []
    
    for _ in range(N):
        A = list(map(int,input().split()))
        if A[0] == 1:
            heapq.heappush(q, -A[1])
        else:
            if q:
                ans.append(-heapq.heappop(q))
            else:
                ans.append(-1)

    print(f'#{t}', *ans)

'''
2
3
1 1
2
2
5
1 3
1 5
2
1 1
2
'''