N = 10
A = [list(map(int,input().split())) for _ in range(N)]

P = [0,5,5,5,5,5]
min_val = 101

def dfs(rc,cnt):
    global min_val
    if rc == 100:
        if min_val > cnt:
            min_val = cnt
        return
    
    if cnt >= min_val:
        return
    
    r = rc // 10
    c = rc % 10
    if A[r][c] == 1:
        for i in range(5,0,-1):
           if is_possible(r,c,i):
                if(P[i] > 0):
                    P[i] -= 1
                    change(r,c,i,0)
                    dfs(rc+1,cnt+1)
                    change(r,c,i,1)
                    P[i] += 1

    else:
        dfs(rc+1,cnt)

def is_possible(r,c,n):
    for i in range(n):
        for j in range(n):
            if (r+i >= 10) or (c+j >= 10):
                return False
            if A[r+i][c+j] != 1:
                return False
    return True

def change(r,c,n,k):
    for i in range(n):
        for j in range(n):
            A[r+i][c+j] = k

dfs(0,0)
ans = -1 if min_val == 101 else min_val
print(ans)