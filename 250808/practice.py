# XYPV
# EOGGXYPBSY

s1 = list(input())
s2 = list(input())

def isInclude(s1, s2):
    for s in s1:
        if s not in s2:
            return False
    return True

print(isInclude(s1, s2))



'''
Q.  첫줄에 N, 다음에 N x N 문자열일 때,
    AB
    CD
    패턴이 존재하는가?
'''
N = int(input())
text = [list(input()) for _ in range(N)]

pattern = [['A','B'],['C','D']]
isSuccess = False
for i in range(N-1):
    for j in range(N-1):
        arr = [[0] * 2 for _ in range(2)]
        for p in range(2):
            for q in range(2):
                arr[p][q] = text[i+p][j+q]
        if arr == pattern :
            isSuccess = True
            break
    if isSuccess:
        break

if isSuccess:
    print("성공")
else:
    print("실패")

'''
Q. 첫 줄에 T, 다음 줄에 N, 다음에 N x N 미로. 0 : 통로, 1 : 벽, # : 로봇, 상하좌우로 모두 이동할 수 있는 칸 수는?
'''
'''
1
5
00101
1#101
00000
00100
00010
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    cnt = 0

    def check(i,j):
        for idx in range(4):
                p = i+dr[idx]
                q = j+dc[idx]
                if 0 <= p < N and 0 <= q < N:
                    if arr[p][q] == '1':
                        return False
        return True

    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] != '1' and check(i,j):
                print(i,j)
                cnt += 1

    print(f'#{t} {cnt}')