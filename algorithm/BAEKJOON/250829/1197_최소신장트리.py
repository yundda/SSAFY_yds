## 최소신장트리
'''
- 에지 리스트로 구현 + 유니온 파인드 
- 사이클이 포함되면 가중치 합이 최소가 될 수 없으므로 사이클 포함 X
- 최소 신장 트리 구성 에지 개수는 항상 **노드개수 -1**
'''
'''
1. 에지 리스트로 데이터 저장
2. 유니온 파인드 리스트 초기화
3. 에지 리스트를 가중치 기준 오름차순으로 정렬
4. s와 e의 대표 노드 확인 후
    같지 않다면, 연결 --> 에지 개수 +1
    같다면, 연결 X (사이클 생김)
5. 가중치 합 출력
'''
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
edges = []
for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append([w,s,e])
    # edges.append([s,e,w])

uf = [i for i in range(V + 1)]

edges.sort()
# edges.sort(key = lambda x:x[2])

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(s,e):
        a = find(s)
        b = find(e)
        if a != b:
            if a > b:
                uf[a] = b
            else:
                uf[b] = a
            return True
        return False


i = 0
ans = 0
for w,s,e in edges:
    if union(s,e):
          cnt += 1
          ans += w
    if cnt == V-1:
         break

print(ans)
