#### 함수 사용 DFS ####
T = 1
for _ in range(T):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))
    A = [-1] * 100
    B = [-1] * 100
    connected = [0] * 100

    # for i in range(len(arr)):
    #     if i % 2 == 1:
    #         if not A[arr[i-1]]:
    #             A[arr[i-1]] = arr[i]
    #         else:
    #             B[arr[i-1]] = arr[i]

    # def dfs(s,e):
    #     if connected[e]:
    #         return 1
    #     connected[s] = 1
    #     for n in range(1,100):
    #         if not connected[n] and (A[s] == n or B[s] == n):
    #             if dfs(n,e):
    #                 return 1

    #     return 0

    for i in range(0, len(arr), 2):
        if A[arr[i]] == -1:
            A[arr[i]] = arr[i + 1]
        else:
            B[arr[i]] = arr[i + 1]

    def dfs(s, e):
        if s == e:
            return 1
        connected[s] = 1
        for n in (A[s], B[s]):
            if (
                n != -1 and not connected[n]
            ):  # 연결 안 된 노드 -1로 저장했었음 connected[-1] 들어가면 XX
                if dfs(n, e):
                    return 1
        return 0

    ans = dfs(0, 99)

    print(f"#{t} {ans}")


#### 스택 사용 DFS ####
T = 1
for _ in range(T):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))
    A = [-1] * 100
    B = [-1] * 100
    connected = [0] * 100

    for i in range(0, len(arr), 2):
        if A[arr[i]] == -1:
            A[arr[i]] = arr[i + 1]
        else:
            B[arr[i]] = arr[i + 1]

    def dfs(s, e):
        if s == e:
            return 1
        stack = [s]
        connected[s] == 1

        while stack:
            cur = stack.pop()
            if cur == e:
                return 1
            for n in (B[cur], A[cur]):
                if n != -1 and not connected[n]:
                    connected[n] == 1
                    stack.append(n)
        return 0

    ans = dfs(0, 99)
    print(f"#{t} {ans}")
