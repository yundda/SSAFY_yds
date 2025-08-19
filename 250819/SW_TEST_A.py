# # N,M,K
# # N개 문제 중 M 개를 맞출 때, K 개를 연속으로 맞추면 누적 점수 2배
# # 가능한 최저 점수는?

N = 8
M = 7
K = 3

# # all_bin = [[(n >> i) & 1 for i in range(N - 1, -1, -1)] for n in range(1 << N)]

# # print(all_bin)

# A = []
# for n in range(1 << N):
#     B = []
#     cnt = 0
#     for i in range(N - 1, -1, -1):
#         B.append((n >> i) & 1)
#     for b in B:
#         if b == 1:
#             cnt += 1
#     if cnt == M:
#         A.append(B)

# min_score = 100000
# for k in range(len(A)):
#     score = 0
#     cnt = 0
#     for i in range(N):
#         quest = A[k][i]
#         if quest == 0:
#             cnt = 0
#         else:
#             cnt += 1
#             score += 1
#             if cnt == K:
#                 cnt = 0
#                 score *= 2
#     if min_score > score:
#         min_score = score

# print(min_score)


def min_score_dp(N, M, K):
    INF = 10**18
    # dp[i][m][r] = 최소 점수
    dp = [[[INF] * K for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for i in range(N):
        for m in range(M + 1):
            for r in range(K):
                s = dp[i][m][r]
                if s == INF:
                    continue
                # 0(틀림)
                if dp[i + 1][m][0] > s:
                    dp[i + 1][m][0] = s
                # 1(맞음) - 정확히 M개만 맞아야 한다면 m < M일 때만
                if m < M:
                    if r + 1 < K:
                        s2, r2 = s + 1, r + 1
                    else:
                        s2, r2 = (s + 1) * 2, 0
                    if dp[i + 1][m + 1][r2] > s2:
                        dp[i + 1][m + 1][r2] = s2

    return min(dp[N][M])  # 어떤 r로 끝나든 최소


ans = min_score_dp(N, M, K)
print(ans)
