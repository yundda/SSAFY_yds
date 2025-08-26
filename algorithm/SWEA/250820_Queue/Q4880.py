T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    def winner(c1, c2):
        if cards[c1] == cards[c2]:
            return c1 if c1 < c2 else c2
        if (
            (cards[c1] == 1 and cards[c2] == 3)
            or (cards[c1] == 2 and cards[c2] == 1)
            or (cards[c1] == 3 and cards[c2] == 2)
        ):
            return c1
        else:
            return c2

    def group(i, j):
        if i == j:
            return i
        mid = (i + j) // 2
        g1 = group(i, mid)
        g2 = group(mid + 1, j)
        w = winner(g1, g2)
        return w

    ans = group(1, N)

    print(f"#{t} {ans}")
