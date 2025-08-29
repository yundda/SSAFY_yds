## 벨만포드 - 음수 가중치가 있어도 수행 가능 & 음수 사이클 존재 여부 판단 가능
'''
엣지 리스트로 그래프 구현
    - E[i] = [출발노드, 종료노드, 가중치]
최단 경로 리스트 초기화
모든 에지 확인 후 정답 리스트 업데이트 => 에지 업데이트 횟수는 **노드개수 - 1** ‼️간선개수아님
음수 사이클 유무 확인
    - 모든 에지를 한번씩 다시 사용해 업데이트 되는지 확인
        - 업데이트 된다 = 음수 사이클 O -> 무한하게 돌수록 가중치 계속 감소 -> 최단거리 도출 X
        - 업데이트 안된다 = 음수 사이클 X
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
E = [0] * M
NV = 10**8
D = [NV] * (N+1)
D[1] = 0

for i in range(M):
    s, e, t = map(int,input().split())
    E[i] = [s,e,t]

# for i in range(N):
#     isMinus = False
#     for s,e,t in E:
#         if D[s] != NV:
#             if D[e] > D[s] + t:
#                 if i == N-1:
#                     isMinus = True
#                 D[e] = D[s] + t

for _ in range(N-1):
    for s,e,t in E:
        if D[s] != NV and D[e] > D[s] + t:
            D[e] = D[s] + t

isMinus = False
for s,e,t in E:
    if D[s] != NV and D[e] > D[s] + t:
        isMinus = True


if isMinus:
    print(-1)
else:                
    for i in range(2,N+1):
        if D[i] == NV:
            print(-1)
        else:
            print(D[i])