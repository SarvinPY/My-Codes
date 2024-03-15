number = int(input("Enter number : "))
for num in range(2,(number//2)+1):
    if number % num == 0:
        print("Not Prime")
        break
else:
    print("Prime") if number != 1 and number != 0 else print("Not Prime")