from heapq import heappop,heappush
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int,input().split())
    nodes = [[] for _ in range(N+1)]
    INF = 10**10
    dist = [INF] * (N+1)
    
    for _ in range(E):
        s,e,w = map(int,input().split())
        nodes[s].append((w,e))

    def dijkstra(start_node):
        hq = []
        heappush(hq,(0,0))
        dist[start_node] = 0

        while hq:
            now_w, now_node = heappop(hq)
            if now_w > dist[now_node]:
                continue
            for nxt_w, nxt_node in nodes[now_node]:
                new_w = now_w + nxt_w
                if dist[nxt_node] <= new_w:
                    continue
                dist[nxt_node] = new_w
                heappush(hq,(dist[nxt_node],nxt_node))

    
    
    dijkstra(0)
    result = dist[N]

    print(f'#{tc} {result}')