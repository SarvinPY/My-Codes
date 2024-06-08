s = [int(x) for x in input().split()]
# n = s[0]
m = s[1]
total = list()
t = [int(x) for x in input().split()]
for k in range(m):
    sum = 0
    a = [int(x) for x in input().split()]
    l = a[0] 
    r = a[1] 
    k = a[2]
    for i in range(l -1 , r , k):
        sum += t[i]
    total.append(sum)
for item in total :
    print(item)