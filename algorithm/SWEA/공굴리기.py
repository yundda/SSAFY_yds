T= int(input())
for t in range(1,T+1):
	N=int(input())
	A=[list(map(int,input().split())) for _ in range(N)]

	dr=[0,0,1,-1]
	dc=[1,-1,0,0]
	
	def in_range(i,j):
		return 0<=i<N and 0<=j<N
	
	def f(r,c,cnt):
		global ans
		min_v=A[r][c]
		mr=-1
		mc=-1
		for k in range(4):
			nr = r+dr[k]
			nc = c+dc[k]

			if in_range(nr,nc):
				if min_v > A[nr][nc]:
					min_v = A[nr][nc]
					mr=nr
					mc=nc
		if min_v==A[r][c]:
			if ans < cnt:
				ans = cnt
			return
		f(mr,mc,cnt+1)
		


	ans = 0
	for i in range(N):
		for j in range(N):
			f(i,j,0)

	print(f'#{t} {ans + 1}')