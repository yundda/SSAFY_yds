# T = int(input())
T = 2
for t in range(1, T + 1):
    N = int(input())
    A = list(input())

    stack = [0] * N
    postfix = ""
    top = -1

    for token in A:
        if top > -1 or token != "+":
            postfix += token
        else:
            top += 1
            stack[top] = token

    while top > -1:
        postfix += stack[top]
        top -= 1

    print(postfix)

    stack = [0] * N
    top = -1

    for token in postfix:
        if token != "+":
            top += 1
            stack[top] = int(token)
        else:
            a = stack[top]
            top -= 1
            b = stack[top]
            stack[top] = b + a

    ans = stack[top]

    print(f"#{t} {ans}")
