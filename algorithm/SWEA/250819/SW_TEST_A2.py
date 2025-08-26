T = int(input())
for t in range(1, T + 1):
    N = int(input())
    Trees = list(map(int, input().split()))
    highest = max(Trees)

    s = 0
    odd = 0
    for tree in Trees:
        diff = highest - tree
        s += diff
        odd += diff % 2

    total_odd = odd * 2 - 1

    if s % 3 == 0:
        total = (s // 3) * 2
    elif s % 3 == 1:
        total = (s // 3) * 2 + 1
    elif s % 3 == 2:
        total = (s // 3) * 2 + 2

    ans = total if total > total_odd else total_odd
    print(f"#{t} {ans}")
