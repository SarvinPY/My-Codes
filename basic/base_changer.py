n = input().split()
num = int(n[0])
base = int(n[1])
count = 1
sum1 = 0
sum2 = 0
while num != 0 :
    r = num % base
    num //= base
    if count % 2 != 0 :
        sum1 += r
    else:
        sum2 += r
    count += 1
if sum1 == sum2 :
    print('Yes')
else :
    print('No')