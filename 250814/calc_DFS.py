infix = "(6+5*(2-8)/2)"
postfix = ""

stack = [0] * 100
top = -1

icp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1}

isp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}

"""
token이 피연산자면,후위식에 추가
연산자라면,
    ')'일 경우,
        '(' 만날 때까지 stack pop + 후위식에 추가
        ')' 버림
    아닐 경우,
        stack[top]보다 우선순위 높을 경우,
            stack에 push
        아닐 경우,
            우선순위 높을 때까지 stack pop + 후위식에 추가
            높아지면, stack에 push
    
    stack에 남은 연산자 모두 출력
"""


for token in infix:
    if token not in "(*/+-)":
        postfix += token
    elif token == ")":
        while top > -1:
            if stack[top] == "(":
                top -= 1
                break
            postfix += stack[top]
            top -= 1

    # else:
    #     if top == -1 or icp[token] > isp[stack[top]]:
    #         top += 1
    #         stack[top] = token
    #     else:
    #         while top > -1:
    #             if icp[token] > isp[stack[top]]:
    #                 break
    #             postfix += stack[top]
    #             top -= 1
    #         top += 1
    #         stack[top] = token

    else:
        while top > -1 and icp[token] <= isp[stack[top]]:
            postfix += stack[top]
            top -= 1
        top += 1
        stack[top] = token

    while top > -1:
        if stack[top] != "(":
            postfix += stack[top]
        top -= 1


print(postfix)
