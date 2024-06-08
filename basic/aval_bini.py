first_number = int(input())
second_number = int(input())
prime_list = []
for i in range(first_number+1 , second_number) :
    count = 0
    for j in range(1 , i+1) :
        if i % j == 0 :
            count += 1
    if count == 2 :
        prime_list.append(i)
for k in range(len(prime_list)) :
    if k != len(prime_list) - 1 :
        print(f'{prime_list[k]},', end='')
    else:
        print(prime_list[k])
