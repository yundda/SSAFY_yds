A = input()

parts = A.split('-')

print(parts)

ans = 0

part1 = map(int,parts[0].split('+'))
for n in part1:
    ans += n

for i in range(1,len(parts)):
    part = map(int,parts[i].split('+'))
    for n in part:
        ans -= n

print(ans)