import sys
sys.stdin = open('input.txt','r')

string = input()
used = {}

for c in string:
    c = c.upper()
    if c in list(used.keys()):
        used[c] += 1
    else:
        used[c] = 1

max_cnt = max(used.values())

ans = ''
for alpha, cnt in used.items():
    if cnt == max_cnt:
        if ans == '':
            ans = alpha
        else:
            ans = '?'
print(ans)
