count = int(input())
name = []
total = []
temp = []
cost = 0
for i in range(count+4):
    detail = input().split()
    if detail[1] != 'Saba' and detail[1] != 'Iman' and detail[1] != 'Mania' and detail[1] != 'Yasin' :
        cost += float(detail[1])
    else:
        name.append(detail[1])
        if i != 0 :
            total.append(cost/4)
            cost = 0
total.append(cost/4)
print(end='        ')
for item in name :
    print(item , end='\t')
print()
for i in range(4):
    temp = []
    temp.append(name[i])
    for j in range(4):
        hesab = total[i] - total[j]
        if hesab == 0:
            temp.append(0)
        elif hesab > 0 :
            temp.append('-')
        else:
            temp.append(-1*hesab)
    for item in temp :
        print(item , end='\t')
    print()
    