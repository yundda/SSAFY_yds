# path = []
# N = 6
# R = 3
# total = 10
# result = 0

# def dice(n,s):
#     global result
#     if n == R and s <= total:
#         result += 1
#         return
#     for i in range(1,7):
#         if s+i > total:
#             continue
#         dice(n+1,s+i)

# dice(0,0)
# print(result)


# path = []
# N = 6
# R = 3
# total = 10
# result = 0


# def dice(n,s):
#     global result
#     if n == R and s <= total:
#         print(path)
#         result += 1
#         return
#     for i in range(1,7):
#         if s+i > total:
#             continue
#         path.append(i)
#         dice(n+1,s+i)
#         path.pop()

# dice(0,0)
# print(result)


cards = ['A', 'J', 'Q', 'K']

R = 5
result = 0
path = []
def choose(n,now,cnt):
    global result
    # if n > 3 and cnt < 2:
    #     return
    if n == R:
        if cnt == 3:
           print(path)
           result += 1
        return
    for i in range(4):
        path.append(cards[i])
        if cnt == 3:
            choose(n+1,i,cnt)
        elif n > 0 and i == now:
            choose(n+1,i,cnt +1)
        else:
            choose(n+1,i,1)
        path.pop()

choose(0,0,1)
print(result)