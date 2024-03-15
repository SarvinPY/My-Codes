number = int(input("Enter a number: "))
binary = 0
while number > 0:
    binary = number % 2 +  binary
    number //= 2
print(binary)