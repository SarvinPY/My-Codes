n = int(input('Enter a number: '))
sum = 0
for i in range(n):
    a = float(input('Enter a point: '))
    sum += a
print(f"class average is {sum/n}")