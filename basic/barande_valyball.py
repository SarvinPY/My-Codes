t = int(input())
result = []
for i in range (t)  :
    n = int(input())
    x = list(input())
    c = x.count('c'.upper())
    q = n - c
    if q > c :
        result.append('Quera')
    else  :
        result.append('CodeCup')
for item in result :
    print(item)
