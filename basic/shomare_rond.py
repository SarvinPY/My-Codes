number_count = int(input())
number_list = []
results_list = []
for i in range(number_count):
    number = int(input())
    number_list.append(number)

for item in number_list :
    f = 0
    count = 0
    y = str(item)
    for i in range(len(y)) :
        count = 0
        for j in range(i+1 , len(y)):
            if y[i] == y[j]:
                count += 1
                if count > 2 :
                    results_list.append('Ronde!')
                    f = 1
                    break
        if f == 1 :
            break
    if f != 1 :
        for i in range(len(y)-2):
            count = 0
            for j in range(i+1 , i+3):
                if y[i] == y[j] :
                    count += 1
            if count > 1 :
                    results_list.append('Ronde!')
                    f = 1
                    break
    count = 0
    if f != 1 :
        x = item
        f = 0
        sum = 0
        while x != 0 :
            r = x % 10
            sum = sum * 10 + r
            x //= 10
            if sum == item :
                results_list.append('Ronde!')
                f = 1
    if f != 1:
        results_list.append('Rond Nist')
for item in results_list :
    print(item)