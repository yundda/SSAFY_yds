import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
A = [[] for _ in range(n+1)]
D = [0] * (n+1)

for _ in range(m):
	a, b = map(int,input().split())
	A[a].append(b)
	D[b] += 1
	

# visited = [False] * (n+1)
			
# k=0
# while k != n:
# 	for i in range(1,n+1):
# 		if D[i]==0 and not visited[i]:
# 			print(i, end = " ")
# 			visited[i] = True
# 			k+=1
# 			for a in A[i]:
# 				D[a] -= 1
# 			break

q = deque()

for i in range(1,n+1):
	if D[i] == 0:
		q.append(i)

while q:
	now = q.popleft()
	print(now, end = " ")
	for a in A[now]:
		D[a] -= 1
		if D[a] == 0:
			q.append(a)

	