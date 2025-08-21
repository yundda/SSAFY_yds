N = 5
A = [i for i in range(1, N + 1)]
bit = [0] * N


# bit[i]를 결정하는 함수
def f(i, N):
    if i == N:
        print(bit)
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0  # 원래대로 복구
        f(i + 1, N)


f(0, N)


def f(i, N):
    if i == N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)
            p[i], p[j] = p[j], p[i]
