T = int(input())
for t in range(1, T + 1):
    string = list(input())
    arr = [0] * len(string)
    top = -1

    for x in string:
        if top > -1 and arr[top] == x:
            top -= 1
        else:
            top += 1
            arr[top] = x

    ans = top + 1
    print(f"#{t} {ans}")
