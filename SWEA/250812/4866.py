T = int(input())
for t in range(1, T + 1):
    string = list(input())
    arr = [0] * len(string)
    top = -1

    dic = {
        "}": "{",
        ")": "(",
    }
    ans = 1
    for x in string:
        if x in ["{", "("]:
            top += 1
            arr[top] = x

        elif x in ["}", ")"]:
            if arr[top] == dic[x]:
                arr[top] = 0
                top -= 1
            else:
                ans = 0
    for x in arr:
        if x == "{" or x == "}" or x == "(" or x == ")":
            ans = 0

    print(f"#{t} {ans}")



########### 복습 ##########

    T = int(input())
for t in range(1,T+1):
    str1 = list(input())
    stack = [0] * len(str1)

    dic = {
        ')' : '(',
        '}' : '{',
    }

    top = -1
    ans = 1
    for x in str1:
        if x in list(dic.keys()):
            if top < 0 or dic[x] != stack[top]:
                    ans = 0
                    break
            else:
                stack[top] = 0
                top -= 1
        elif x in list(dic.values()):
            top += 1
            stack[top] = x

    print(stack)

    for x in stack:
        if x in list(dic.keys()) or x in list(dic.values()):
            ans = 0

    print(ans)

