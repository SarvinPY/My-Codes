# sentence = input().split()
# word = input()
# length = len(word) - 1
# count = 0
# for item in sentence :
#     if len(item) >= length :
#         if ord(word[0]) == ord(item[0]) or ord(word[0])+ 32  == ord(item[0]) or ord(word[0]) == ord(item[0]) + 32 :                
#             count += 1
#         elif ord(word[0]) == ord(item[length]) or ord(word[0]) + 32 == ord(item[length]) or ord(word[0]) == ord(item[length]) + 32 :
#             count += 1 
# print(count)
sentence = input().split()
word = input()
length = len(word) - 1
count = 0
for item in sentence :
    if len(item) >= 8 :
        if (word[0] == item[0] and word[length] == item[length]) or (word[0].lower == item[0].lower and word[length].lower == item[length].lower)  :                
            count += 1
        elif (word[0] == item[length] and word[length] == item[0]) or (word[0].lower() == item[length].lower() and word[length].lower() == item[0].lower()) :
            count += 1 
print(count)
# sentence = input().split()
# word = input()
# length = len(word) - 1
# count = 0
# for item in sentence :
#     if len(item) >= 0 :
#         a = word[0].lower()
#         b = item[0].lower()
#         if word[0] == item[0] or a == b :                
#             count += 1
#         elif word[0] == item[length] or word[0].lower == item[length].lower :
#             count += 1 
# print(count)
# print(a , b)

