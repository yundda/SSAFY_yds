#### 파이썬에서 시간 초과 ==> Binary Lifting LCA 풀이 필요

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
A = [[] for _ in range(N+1)]
for _ in range(N-1):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)


q = deque()
visited = [False] * (N+1)
q.append(1)
tree = [0] * (N+1)
tree[1] = (0,0)

while q:
    par = q.popleft()
    depth = tree[par][1]
    visited[par] = True
    for child in A[par]:
        if not visited[child]:
            tree[child] = (par,depth+1)
            q.append(child)


def find_par_same_depth(a,d,depth):
    while d != depth:
        a = tree[a][0]
        d = tree[a][1]
    return a

M = int(input())
for _ in range(M):
    a, b = map(int,input().split())
    par_a, dep_a = tree[a]
    par_b, dep_b = tree[b]
    if par_a != par_b:
        if dep_a > dep_b:
            a = find_par_same_depth(a,dep_a,dep_b)
        elif dep_a < dep_b:
            b = find_par_same_depth(b,dep_b,dep_a)
    while a != b:
        a = tree[a][0]
        b = tree[b][0]

    print(a)

  