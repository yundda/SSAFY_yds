# # 250806
# import copy

# T = int(input())
# for t in range(1, T + 1):
#     puzzle = [list(map(int, input().split())) for _ in range(9)]

#     compare = [i for i in range(1, 10)]

#     N = 9

#     # compare와 비교하기 위해 순서대로 정렬
#     def sorting(puzzle):
#         # sorted_puzzle = puzzle.copy()
#         for i in range(N - 1, -1, -1):
#             for j in range(i):
#                 if puzzle[j] > puzzle[j + 1]:
#                     puzzle[j], puzzle[j + 1] = puzzle[j + 1], puzzle[j]
#         return puzzle

#     # 전치 행렬
#     def chg_r_c(puzzle):
#         # chg_puzzle = puzzle.copy()
#         for r in range(9):
#             for c in range(9):
#                 if r > c:
#                     puzzle[r][c], puzzle[c][r] = puzzle[c][r], puzzle[r][c]
#         return puzzle

#     # 행 비교 : 각 행 접근 후 sorting()
#     def check_row(puzzle):
#         for row in puzzle:
#             print(row)
#             if sorting(row) != compare:
#                 print("실패")
#                 return False
#         return True

#     # 열 비교 :전치 행렬 후 행 비교
#     def check_col(puzzle):
#         chg_puzzle = chg_r_c(puzzle)
#         return check_row(chg_puzzle)

#     # 각 사각형 비교
#     def check_square(puzzle):
#         global isCheck
#         for i in range(3):
#             r = i * 3
#             for j in range(3):
#                 c = i * 3
#                 arr = [0] * 9
#                 for p in range(3):
#                     for q in range(3):
#                         arr[puzzle[r + p][c + q] - 1] += 1
#                 if arr != [1 for _ in range(9)]:
#                     print("실패")
#                     return False
#         return True

#     # isCheck = True
#     # if isCheck:
#     #     copy_puzzle = copy.deepcopy(puzzle)
#     #     print(isCheck)
#     #     check_row(copy_puzzle)
#     #     if isCheck:
#     #         copy_puzzle = copy.deepcopy(puzzle)
#     #         print(isCheck)
#     #         check_col(copy_puzzle)
#     #         if isCheck:
#     #             copy_puzzle = copy.deepcopy(puzzle)
#     #             print(isCheck)
#     #             check_square(copy_puzzle)

#     ans = 0
#     copy_puzzle = copy.deepcopy(puzzle)
#     if check_row(copy_puzzle):
#         print("1. 성공")
#         copy_puzzle = copy.deepcopy(puzzle)
#         if check_col(copy_puzzle):
#             print("2. 성공")
#             copy_puzzle = copy.deepcopy(puzzle)
#             if check_square(copy_puzzle):
#                 ans = 1

#     print(f"#{t} {ans}")


######## 카운트로 풀기 #########
# 250813
T = int(input())
N = 9
for t in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    cor = [i for i in range(1, 10)]

    def isFailed(A):
        count = [0] * (N + 1)
        for i in range(N):
            count[A[i]] += 1

        for n in count:
            if n > 1:
                return True

    def my_func():
        for i in range(N):
            A = [arr[i][j] for j in range(N)]
            if isFailed(A):
                return 0

        for j in range(N):
            A = [arr[i][j] for i in range(N)]
            if isFailed(A):
                return 0

        for i in range(3):
            for j in range(3):
                count = [0] * (N + 1)
                for p in range(3):
                    for q in range(3):
                        x = arr[3 * i + p][3 * j + q]
                        count[x] += 1
                        if count[x] > 1:
                            return 0
        return 1

    ans = my_func()

    print(f"#{t} {ans}")
