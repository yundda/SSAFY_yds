N = int(input())
nums = [int(input()) for _ in range(N)]

stack = []
ans = []
i = 1
isFailed = False
for n in nums:
    if not stack:
        if i > N:
            isFailed = True
            break
        stack.append(i)
        ans.append("+")
        i += 1
    if stack[-1] < n:
        while stack[-1] != n:
            if i > N:
                isFailed = True
                break
            stack.append(i)
            ans.append("+")
            i += 1
    elif stack[-1] > n:
        isFailed = True
        break
    if isFailed:
        break
    if stack[-1] == n:
        stack.pop()
        ans.append("-")


if isFailed:
    print("NO")
else:
    for a in ans:
        print(a)
