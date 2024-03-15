n = input()
sum = int(n)
while sum > 9 :
    n = list(n)
    n = [int(x) for x in n]
    sum = 0
    for i in range(len(n)):
        sum += n[i]
    n = str(sum)
print(sum)