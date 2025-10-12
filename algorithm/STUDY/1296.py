import sys
sys.stdin = open('input.txt','r')

yeondoo = input()
N = int(input())
names = [0] * N

for i in range(N):
    names[i] = input()

def counting(name):
    count = {'L':0,'O':0,'V':0,'E':0}
    for alpha in name:
        if alpha == 'L':
            count['L'] += 1
        elif alpha == 'O':
            count['O'] += 1
        elif alpha == 'V':
            count['V'] += 1
        elif alpha == 'E':
            count['E'] += 1
    return count


def percentage(A,B):
    l = A['L'] + B['L']
    o = A['O'] + B['O']
    v = A['V'] + B['V']
    e = A['E'] + B['E']

    val = ((l+o) * (l+v) *(l+e) * (o+v) * (o+e) * (v+e)) % 100
    return val


Y = counting(yeondoo)
max_p = -1
for name in names:
    count = counting(name)
    p = percentage(Y,count)

    if max_p < p:
        max_p = p
        ans = name
    elif max_p == p:
        ans = min(ans,name)


print(ans)
