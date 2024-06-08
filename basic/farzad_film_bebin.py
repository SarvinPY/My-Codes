n = int(input())
final = []
for i in range(n) :
    name = input().split()
    temp = []
    for film in name :
        corrected_name = ''
        for index in range(len(film)) :
            if index == 0 :
                corrected_name += film[0].upper()
            else:
                corrected_name += film[index].lower()
        temp.append(corrected_name)
    final.append(temp)
for item in final :
    for correct in item :
        print(correct , end=' ')
    print()