input = [int(x) for x in input().split()]
number_list = []
number_count = 0
base = input[1]
if base == 10 :
    for i in range(2 , 10000) :
        count = 0
        for j in range(1 , i+1) :
            if i % j == 0 :
                count += 1
        if count == 2 :
            if 1 < i < 10 :
                number_list.append(i)
                number_count += 1
            else :
                i = str(i)
                last = i
                i = i[::-1]
                if last == i :
                    number_list.append(int(last))
                    number_count += 1
        if number_count == input[0] :
            index = input[0] - 1
            print(number_list[index])
            break
else:
    for i in range(2 , 10000) :
        count = 0
        for j in range(1 , i+1) :
            if i % j == 0 :
                count += 1
        if count == 2 :
            sum = ''
            prime = i
            while i != 0:
                r = i % base
                sum += str(r)
                i //= base
            a_sum = sum[::-1]
            if sum == a_sum :
                number_list.append(prime)
                number_count += 1
        if number_count == input[0] :
            index = input[0] - 1
            print(number_list[index])
            break