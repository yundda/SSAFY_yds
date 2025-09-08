Friend = ['A','B','C','D','E']
result = 0

# for i in range(1<<len(Friend)):
#     a = []
#     cnt = 0
#     for idx in range(len(Friend)):
#         if i & (1<<idx):
#             a.append(Friend[idx])
#             cnt += 1
#     if cnt >=2:
#         result += 1

# print(result)
            
path = []
def recur(cnt, start):
    global result
    if cnt >= 2:
        print(*path)
        result += 1
    
    for i in range(start, len(Friend)):
        path.append(Friend[i])
        recur(cnt + 1, i+1)
        path.pop()
    
recur(0,0)
print(result)
