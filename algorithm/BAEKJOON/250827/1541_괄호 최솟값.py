A = input()

numstr = ''
ans = 0

is_minus = False
for i in range(len(A)): 
    if A[i] == '-' and not is_minus: # 첫 '-' 인 경우
        ans += int(numstr)
        numstr = ''
        is_minus = True

    elif A[i] in '+-': # '+-' 인 경우
        if is_minus:
            ans -= int(numstr)
        else:
            ans += int(numstr)
        numstr = ''

    else: # 숫자인 경우
        numstr += A[i]

if is_minus:
    ans -= int(numstr)
else:
    ans += int(numstr)

print(ans)