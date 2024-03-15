n = int(input())
f1 = 0
f2 = 1
total = 0
for i in range(n) :
    print(f1 , end= " ")
    total = f1 + f2
    f1 = f2
    f2 = total