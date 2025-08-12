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
