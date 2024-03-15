chars = input()
char = list(chars)
n = int(input())
for i in range(1 , n+1):
    for j in range(n-i+1):
        print(" " , end='')
    for k in range(i):
        if k % len(char) < len(char) :
            print(char[k % len(char)] , end= ' ')
    print()
for n in range(n):
    print(' ' , end='')
print('|')