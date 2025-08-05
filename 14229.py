# 250805
nums = list(map(int, input().split()))
print(nums)
N = len(nums)
# k = 1000000
k = 10
c = [ 0 ] * ( k + 1 )
A = [ 0 ] * (N) 

for i in range(N):
    c[nums[i]] += 1
    
for i in range(1, k+1):
    c[i] += c[i-1]

for i in range(N-1, -1, -1):
    num = nums[i]
    c[ num ] -= 1
    A[c[ num ]] = num
    
# print(A[50000])
print(A)

    