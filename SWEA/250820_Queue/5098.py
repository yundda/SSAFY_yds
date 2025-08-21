# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     cheese = list(map(int, input().split()))

#     in_machine = [i for i in range(N)]
#     melted = [0] * M
#     front = 0
#     out = 0
#     while True:
#         if out == M - 1:
#             break
#         if in_machine[front] > -1:
#             cheese[in_machine[front]] //= 2
#             if cheese[in_machine[front]] == 0:
#                 out += 1
#                 melted[in_machine[front]] = 1
#                 in_machine[front] = (N - 1) + out if (N - 1) + out < M else -1
#         front = (front + 1) % N

#     for i in range(M):
#         if melted[i] == 0:
#             ans = i + 1

#     print(f"#{t} {ans}")


from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    machine = deque()
    for i in range(N):
        machine.append((i, cheese[i]))
    # machine = deque([(i,cheese[i]) for i in range(N)])

    next_idx = N
    last_idx = -1

    while machine:
        idx, chz = machine.popleft()
        chz //= 2
        if chz == 0:
            last_idx = idx
            if next_idx < M:
                machine.append((next_idx, cheese[next_idx]))
                next_idx += 1
        else:
            machine.append((idx, chz))

    print(f"#{t} {last_idx+1}")
