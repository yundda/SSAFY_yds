A = [1,2,3]
path = []
used = [False] * len(A)
N = 0
def p(n):
    if n == 2:
        print(path)
        return
    for i in range(len(A)):
        # 시간 복잡도 터짐!
        # if A[i] in path:
        #     continue
        # if used[i]:
        #     continue
        if not used[i]:
            path.append(A[i])
            used[i] = True
            p(n+1)
            path.pop()
            used[i] = False

p(N)