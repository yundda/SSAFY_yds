import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
A=[[] for _ in range(N+1)]
visited=[False]*(N+1)
parents=[0]*(N+1)

for _ in range(N-1):
	s,e=map(int,input().split())
	A[s].append(e)
	A[e].append(s)
	
q=deque()
q.append(1)

while q:
	par=q.pop()
	visited[par]=True
	
	for child in A[par]:
		if not visited[child]:
			parents[child]=par
			q.append(child)
			
for i in range(2,N+1):
	print(parents[i])
			