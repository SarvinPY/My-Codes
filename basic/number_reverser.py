num = int(input("Enter number : "))
n_num = 0
while num != 0:
    n_num *= 10             
    n_num += (num % 10)     
    num //= 10              
print(n_num)
