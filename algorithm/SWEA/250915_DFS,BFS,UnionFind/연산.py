from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    
    def BFS(x):
        q = deque()
        q.append((x,0))
        visited = [False] * 1000001
        visited[x] = True
        
        while q:
            val,cnt = q.popleft()
            nxt_val = [val+1,val-1,val*2,val-10]
            for v in nxt_val:
                if v == M:
                    return cnt+1
                if 1 <= v <= 1000000 and not visited[i]:
                    q.append((v,cnt+1))
                    visited[v] = True
                
    ans = BFS(N)
    print(f'#{tc} {ans}')