a = input().split()
b = input().split()
c = input().split()
f = 0
if (a[0] == b[1] == c[2]) or (a[2] == b[1] == c[0]) :
    if a[0] == "x" or a[2] == "x":
        print("Player x Won!")
        f = 1
    else:
        print("Player o Won!")
        f = 1
elif (a[0] == a[1] == a[2] ) or (b[0] == b[1] == b[2] ) or (b[0] == b[1] == b[2] ) :
    if a[0] == "x" or b[0] == "x" or c[0] == "x" :
        print("Player x Won!")
        f = 1
    else :
        print("Player o Won!")
        f = 1
else :
    for i in range(3):
        if (a[i] == b[i] == c[i] == "x") :
            print("Player x Won!")
            f = 1
        elif (a[i] == b[i] == c[i] == "o") :
            print("Player o Won!")
            f = 1
if f == 0 :
    print("Draw.")