n = int(input())
m = [int(x) for x in input().split()]
count = 0
bede = 0
zarf = 0
for i in range(n) :
    if m[i] > 0 and count == 0:
        bede += m[i]
    elif m[i] > 0:
        if m[i] > zarf :
            bede = bede + (m[i] - zarf)
            zarf = 0
        elif zarf > m[i] :
            zarf -= m[i]
    elif m[i] < 0:
        zarf += abs(m[i])
        count += 1
print(bede)
