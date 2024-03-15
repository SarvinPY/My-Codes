num = int(input("Enter number : "))
if num < 0 :
    num = -num

square = num**2

while num > 0:
    digit_1 = num % 10
    digit_2 = square % 10

    # Check digit by digit until num == 0
    if digit_1 != digit_2:
        print("Not")
        break

    num //= 10
    square //= 10
else:
    print("Automorphic.")