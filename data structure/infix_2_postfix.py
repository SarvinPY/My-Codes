#Sarvin_Hosseini
#AP
#Infix to postfix

def precedence(chr):
        if chr == '+' or chr == '-' :
            return 1
        elif chr == '*' or chr ==  '/' :
            return 2
        elif chr == '^':
            return 3
        else :
            return 0


def postfix_2_answer(infix):
# infix to postfix :

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
            while len(stack) != 0 and precedence(stack[-1]) >= precedence(char) :
                postfix += stack.pop()
                postfix += ' '
            stack.append(char)
            last = ''
    postfix += last
    postfix += ' '
    while len(stack) != 0 :
        postfix += stack.pop()
        postfix += ' '
#---------------------------------------------------------
#this part : by using stack , calculatint (postfix to answer)
    stack = []
    for item in postfix.split():
        answer = 0
        if item == '+' :
            answer += stack.pop(-2) + stack.pop()
            stack.append(answer)
        elif item == '-' :
            answer += stack.pop(-2) - stack.pop()
            stack.append(answer)
        elif item == '*' :
            answer += stack.pop(-2) * stack.pop()
            stack.append(answer)
        elif item == '/' :
            answer += stack.pop(-2) / stack.pop()
            stack.append(answer)
        elif item == '^' :
            answer += stack.pop(-2) ** stack.pop()
            stack.append(answer)
        else:
            item = int(item)
            stack.append(float(item))
    return answer

#for test: print(postfix_2_answer("11+2*(1^3-0)^(7+4*2)-4"))