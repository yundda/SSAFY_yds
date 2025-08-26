T = 1
for t in range(1, T + 1):
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    cnt = 0

    for j in range(M):
        stack = []
        A = [arr[i][j] for i in range(M)]
        for a in A:
            if a != 0:
                stack.append(a)
                if stack[0] == 2:
                    stack.pop(0)
                if len(stack) > 1 and stack[-2] + a == 3 and a == 2:
                    cnt += 1

    print(f"#{t} {cnt}")
