A = [1,3,5,2]
N = len(A)
for i in range(1<<N): # 1 << N = 16 
    a = []
    s = 0
    for idx in range(N):
        if i & (1<<idx):
            a.append(A[idx])
            s += A[idx]
    if s == 5:
        print(a)