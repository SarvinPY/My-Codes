count = int(input())
final = {}
course = []
sum = 0
n = -1
t = [22 , 21 , 63 , 30]
for i in range(count+4):
    a = input().split()
    if a[0] == '-':
        n += 1
        sum = 0
        last = a[1]
        final[a[1]] = t[n]-sum
    else:
        sum += int(a[1])
        final[last] = t[n]-sum
for key , value in final.items():
    print(f'{key} : {value}')