k = int(input())
sum = 0
for i in range(1 , 1000):
    count = 0
    sum += i
    for j in range(1 , sum+1) :
        if sum % j == 0 :
            count += 1
    if count >= k :
        print(sum)
        break