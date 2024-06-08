# def infix_to_postfix(expression):
#     # تعریف اولویت عملگرها
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
#     stack = []  # پشته برای عملگرها
#     output = []  # لیست خروجی برای عبارت postfix

#     for char in expression:
#         if char.isalnum():  # اگر کاراکتر یک عدد یا حرف باشد، به خروجی اضافه می‌شود
#             output.append(char)
#         elif char == '(':  # اگر کاراکتر پرانتز باز باشد، به پشته اضافه می‌شود
#             stack.append(char)
#         elif char == ')':  # اگر کاراکتر پرانتز بسته باشد، از پشته تا پرانتز باز استخراج می‌کنیم
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             stack.pop()  # پرانتز باز را از پشته حذف می‌کنیم
#         else:  # اگر کاراکتر یک عملگر باشد
#             while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
#                 output.append(stack.pop())
#             stack.append(char)

#     # تمام عملگرهای باقی‌مانده در پشته را به خروجی اضافه می‌کنیم
#     while stack:
#         output.append(stack.pop())

#     return ''.join(output)

# # تست کد با عبارت داده شده
# expression = "a+b*(c^d-e)^(f+g*h)-i"
# postfix = infix_to_postfix(expression)
# print(postfix)
# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
# def binarySearch (arr, l, r, x): 
  
#     # Check base case 
#     if r >= l: 
  
#         mid = l + (r - l)/2
  
#         # If element is present at the middle itself 
#         if arr[mid] == x: 
#             return mid 
          
#         # If element is smaller than mid, then it  
#         # can only be present in left subarray 
#         elif arr[mid] > x: 
#             return binarySearch(arr, l, mid-1, x) 

#         # Else the element can only be present  
#         # in right subarray 
#         else: 
#             return binarySearch(arr, mid + 1, r, x) 
  
#     else: 
#         # Element is not present in the array 
#         return -1
  
# # Test array 
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# if result != -1: 
#     print("Element is present at index % d" % result )
# else: 
#     print("Element is not present in array")



#Sarvin_Hosseini
#AP
#Infix to postfix


class Calculat :

    def precedence(self , chr):
        if chr == '+' or chr == '-' :
            return 1
        elif chr == '*' or chr ==  '/' :
            return 2
        elif chr == '^':
            return 3
        else :
            return 0

    def infix_2_postfix(self , infix):
        stack = []
        postfix = ''
        last = ''
        for char in infix :
            if char.isalnum() :
                last += char
            elif char == '(' :
                stack.append(char)
            elif char == ")" :
                postfix += ' '
                postfix += last
                postfix += ' '
                last = ''
                while stack[-1] != "(":
                    postfix += stack.pop()
                    postfix += ' '
                stack.pop()
            else:
                postfix += last
                postfix += ' '
                while len(stack) != 0 and self.precedence(stack[-1]) >= self.precedence(char) :
                    postfix += stack.pop()
                    postfix += ' '
                stack.append(char)
                last = ''
        postfix += last
        postfix += ' '
        while len(stack) != 0 :
            postfix += stack.pop()
            postfix += ' '
        return postfix.split()
    def postfix_2_answer(self , infix_2_postfix):
        stack = []
        answer = 0
        for item in infix_2_postfix:
            if item == '+' :
                answer += stack.pop() + stack.pop()
                stack.append(answer)
            elif item == '-' :
                answer += stack.pop() + stack.pop()
                stack.append(answer)
            elif item == '*' :
                answer += stack.pop() + stack.pop()
                stack.append(answer)
            elif item == '/' :
                answer += stack.pop() + stack.pop()
                stack.append(answer)
            elif item == '^' :
                answer += stack.pop() + stack.pop()
                stack.append(answer)
            else:
                item = int(item)
                stack.append(float(item))
        return answer





x = Calculat()
# y = x.infix_2_postfix("11+2*(1^3-0)^(7+4*2)-4")
print(x.postfix_2_answer("11+2*(1^3-0)^(7+4*2)-4"))
