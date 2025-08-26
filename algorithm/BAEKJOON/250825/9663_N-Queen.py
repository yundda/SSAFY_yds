N = int(input())

visited_col = [False] * N
cross1 = [False] * 2*N
cross2 = [False] * 2*N



def f(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for next_col in range(N):
        if not visited_col[next_col] and not cross1[(row - next_col) + (N - 1)] and not cross2[row + next_col]:
            visited_col[next_col] = cross1[(row - next_col) + (N - 1)] = cross2[row + next_col] = True
            f(row+1)
            visited_col[next_col] = cross1[(row - next_col) + (N - 1)] = cross2[row + next_col] = False
    return

cnt = 0
f(0)

print(cnt)