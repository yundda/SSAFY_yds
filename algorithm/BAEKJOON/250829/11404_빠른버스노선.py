## 플로이드 워셜
'''
**모든 노드 간 최단 경로 탐색** = 출발지 X
=> 시간 복잡도 V^3 -> 노드 개수가 작을 때
음수 가중치 있어도 수행 가능
점화식 + 동적 계획법 사용
'''
'''
##### 1->5 최단 경로일 경우, 1->5 최단경로 = 1->4 최단경로 + 4->5 최단경로
1. 리스트 선언 및 초기화 (인접 행렬 사용)
    - S와 E 값이 같은 곳은 0, 다른 칸 무한
2. 최단 거리 리스트에 그래프 데이터 저장
3. 점화식으로 리스트 업데이트
'''
n = int(input())
m = int(input())
NV = 10**10
A = [[NV] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    A[i][i] = 0

for _ in range(m):
    s,e,c = map(int,input().split())
    if A[s][e] > c:     # ‼️POINT! 같은 s, e 에 다른 c가 들어올 수 있음
        A[s][e] = c

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if A[s][e] > A[s][k] + A[k][e]:
                A[s][e] = A[s][k] + A[k][e]

for i in range(1,n+1):
    for j in range(1,n+1):
        if A[i][j] == NV:
            print(0, end = " ")
        else:
            print(A[i][j], end = " ")
    print()