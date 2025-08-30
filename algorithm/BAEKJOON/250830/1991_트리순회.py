import sys
input=sys.stdin.readline

N=int(input())
A=[[] for _ in range(N+1)]



def preorder(node):
	if node < 0:
		return
	print(chr(ord('A')+node), end="")
	preorder(A[node][0])
	preorder(A[node][1])
	
def inorder(node):
	if node < 0:
		return
	inorder(A[node][0])
	print(chr(ord('A')+node), end="")
	inorder(A[node][1])
	
def postorder(node):
	if node < 0:
		return
	postorder(A[node][0])
	postorder(A[node][1])
	print(chr(ord('A')+node), end="")


for _ in range(N):
	n,l,r =map(ord,input().split())
	n -= ord('A')
	l -= ord('A')
	r -= ord('A')
	A[n].append(l)
	A[n].append(r)
	
	



preorder(0)
print()
inorder(0)
print()
postorder(0)
