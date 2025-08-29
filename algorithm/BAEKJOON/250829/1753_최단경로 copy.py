### 다익스트라
'''
거리 리스트에서 D가 가장 작은 노드 선택 -> 우선순위 큐에서 추출
이미 더 짧은 거리로 방문됨 → 무시
최단 거리 비교 후 업데이트 -> 업데이트 시, 큐에 삽입
큐가 빌 때까지 반복

'''



import sys, heapq
input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

G = [[] for _ in range(V + 1)]
INF = 10**8
D = [INF] * (V+1)
D[K] = 0

for _ in range(E):
    u,v,w = map(int,input().split())
    G[u].append((v,w))

q = []
heapq.heappush(q,(0, K))

while q:
    d, node = heapq.heappop(q)
    if d > D[node]:
        continue
    for nxt_n, nxt_w in G[node]:
        if D[nxt_n] > nxt_w + d:
            D[nxt_n] = nxt_w + d
            heapq.heappush(q,(D[nxt_n],nxt_n))

for i in range(1, V+1):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])
