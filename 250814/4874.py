T = int(input())
for t in range(1, T + 1):
    postfix = list(input().split())
    stack = [0] * len(postfix)
    top = -1
    ans = "error"

    for token in postfix:
        if token not in "+*-/.":
            top += 1
            stack[top] = int(token)
        elif token != ".":
            if top < 1:
                ans = "error"
                break
            a = stack[top]
            top -= 1
            b = stack[top]
            if token == "*":
                result = b * a
            elif token == "/":
                result = b / a
            elif token == "+":
                result = b + a
            elif token == "-":
                result = b - a
            stack[top] = result

        elif token == ".":
            if top == 0:
                ans = int(stack[top])
            else:
                ans = "error"
            break
    else:
        ans = "error"

    print(f"#{t} {ans}")
