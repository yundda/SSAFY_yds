### pop & append로 풀기
T = 10
for t in range(1, T + 1):
    N = int(input())
    calc = list(input())

    postfix = ""
    stack = []
    dict = {
        "*": 1,
        "+": 0,
    }

    for token in calc:
        if token not in "+*":
            postfix += token
        else:
            while len(stack) > 0 and dict[token] <= dict[stack[-1]]:
                postfix += stack.pop()
            stack.append(token)

    while stack:
        postfix += stack.pop()

    for token in postfix:
        if token not in "+*":
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(b + a)
            elif token == "*":
                stack.append(b * a)

    print(f"#{t} {stack[-1]}")


### top 으로 풀기

T = 10
for t in range(1, T + 1):
    N = int(input())
    calc = list(input())

    postfix = ""
    stack = [0] * N
    top = -1
    dict = {
        "*": 1,
        "+": 0,
    }

    for token in calc:
        if token not in "+*":
            postfix += token
        else:
            while top > -1 and dict[token] <= dict[stack[top]]:
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = token

    while top > -1:
        postfix += stack[top]
        top -= 1

    top = -1
    for token in postfix:
        if token not in "+*":
            top += 1
            stack[top] = int(token)
        else:
            a = stack[top]
            top -= 1
            b = stack[top]
            top -= 1
            if token == "+":
                top += 1
                stack[top] = b + a
            elif token == "*":
                top += 1
                stack[top] = b * a

    print(f"#{t} {stack[top]}")
