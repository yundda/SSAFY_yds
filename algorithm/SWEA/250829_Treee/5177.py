T = 1
for t in range(1,T + 1):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    stack = []
    calc = ''
    def inorder(n):
        if n == 0:
            return
        inorder(tree[n][1])
        inorder(tree[n][2])
        val = tree[n][0]
        if val not in '+-*/':
            stack.append(int(val))
        else:
            a = stack.pop()
            b = stack.pop()
            if val == '*':
                stack.append(b * a)
            if val == '/':
                stack.append(b / a)
            if val == '+':
                stack.append(b + a)
            if val == '-':
                stack.append(b - a)
    
    for _ in range(N):
        info = list(input().split())
        if len(info) == 2:        
            n, x, l, r =  int(info[0]), info[1], 0, 0
        else:
            n, x, l, r = int(info[0]),info[1], int(info[2]), int(info[3])

        tree[n].append(x)
        tree[n].append(l)
        tree[n].append(r)
    

    inorder(1)
    ans = int(stack[0])

    print(f'#{t} {ans}')

'''
5
1 - 2 3
2 - 4 5
3 10
4 88
5 65
'''