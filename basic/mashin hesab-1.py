# import math
# n=input()
# a=[['+','-'],['*','/'],['**','//'],['sin','cos','tsn'],['log','ln']]
# if n=='guid':
#      for i in range(len(a)):
#         for j in range(len(a[i])):
#              print(a[i][j],end='\t')
#         print(sep='') 
# m=[]
# m.append(n)
# while n!='=':
#     n=input()
#     m.append(n)
# m.pop()
# print(m)
# if len(m)!=1:


#     if len(m)==2:
#         while 'sin' in m:
#             a=m.index('sin')
#             c=math.radians(float(m[a+1]))
#             c1=math.sin(c)
#             del m[a]
#             del m[a]
#             m.insert(a,c1)
#     elif len(m)>2:
#         while 'sin' in m:
#             a=m.index('sin')
#             c=math.radians(float(m[a+1]))
#             c1=math.sin(c)
#             c2=round(c1,2)
#             del m[a]
#             del m[a]
#             m.insert(a,c2)
#     if len(m)==2:
#         while 'cos' in m:
#             a=m.index('cos')
#             c=math.radians(float(m[a+1]))
#             c1=math.cos(c)
#             del m[a]
#             del m[a]
#             m.insert(a,c1)
#     elif len(m)>2:
#         while 'cos' in m:
#             a=m.index('cos')
#             c=math.radians(float(m[a+1]))
#             c1=math.cos(c)
#             c2=round(c1,2)
#             del m[a]
#             del m[a]
#             m.insert(a,c2)
#     if len(m)==2:
#         while 'tan' in m:
#             a=m.index('tan')
#             c=math.radians(float(m[a+1]))
#             c1=math.tan(c)
#             del m[a]
#             del m[a]
#             m.insert(a,c1)
#     elif len(m)>2:
#         while 'tan' in m:
#             a=m.index('tan')
#             c=math.radians(float(m[a+1]))
#             c1=math.tan(c)
#             c2=round(c1,2)
#             del m[a]
#             del m[a]
#             m.insert(a,c2)



#     if len(m)==3:
#         while 'log' in m :
#             a=m.index('log')
#             c=math.log(float(m[a+1]),int(m[a+2]))
#             del m[a]
#             del m[a]
#             del m[a]
#             m.insert(a,c)
#     elif len(m)>3:
#         while 'log' in m :
#             a=m.index('log')
#             c=math.log(float(m[a+1]),int(m[a+2]))
#             c1=round(c,2)
#             del m[a]
#             del m[a]
#             del m[a]
#             m.insert(a,c1)

#     if len(m)==2:
#         if 'ln' in m :
#             a=m.index('ln')
#             c=math.log(float(m[a+1]))
#             del m[a]
#             del m[a]
#             m.insert(a,c)
#     elif len(m)>2:
#          while 'ln' in m :
#             a=m.index('ln')
#             c=math.log(float(m[a+1]))
#             c1=round(c,2)
#             del m[a]
#             del m[a]
#             m.insert(a,c1)

         


#     while ('**' in m) and ('//' in m) and (m.index('**'))<(m.index('//')):
#             if '//' in m :
#                 a=m.index('//')
#                 c=math.sqrt(float(m[a+1]))
#                 del m[a]
#                 del m[a]
#                 m.insert(a,c)

#             elif '**' in m :
#                 a=m.index('**')
#                 c=float(m[a-1])**float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#     while ('**' in m) and ('//' in m) and (m.index('**'))>(m.index('//')):
#             if '**' in m :
#                 a=m.index('**')
#                 c=float(m[a-1])**float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#             elif '//' in m :
#                 a=m.index('//')
#                 c=math.sqrt(float(m[a+1]))
#                 del m[a]
#                 del m[a]
#                 m.insert(a,c)
#     while '**' in m :
#         a=m.index('**')
#         c=float(m[a-1])**float(m[a+1])
#         del m[a]
#         del m[a]
#         del m[a-1]
#         m.insert(a-1,c)
#     while '//' in m :
#         a=m.index('//')
#         c=math.sqrt(float(m[a+1]))
#         del m[a]
#         del m[a]
#         m.insert(a,c)


#     while ('*' in m) and ('/' in m) and (m.index('*'))<(m.index('/')):
#             if '/' in m :
#                 a=m.index('/')
#                 c=float(m[a-1])/float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#             elif '*' in m :
#                 a=m.index('*')
#                 c=float(m[a-1])*float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#     while ('*' in m) and ('/' in m) and (m.index('*'))>(m.index('/')):
#             if '*' in m :
#                 a=m.index('*')
#                 c=float(m[a-1])*float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#             elif '/' in m :
#                 a=m.index('/')
#                 c=float(m[a-1])/float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#     while '/' in m :
#             a=m.index('/')
#             c=float(m[a-1])/float(m[a+1])
#             del m[a]
#             del m[a]
#             del m[a-1]
#             m.insert(a-1,c)
#     while '*' in m :     
#             a=m.index('*')
#             c=float(m[a-1])*float(m[a+1])
#             del m[a]
#             del m[a]
#             del m[a-1]
#             m.insert(a-1,c)



#     while ('+' in m) and ('-' in m) and (m.index('+'))<(m.index('-')):
#             if '+' in m :
#                 a=m.index('+')
#                 c=float(m[a-1])+float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#             elif '-' in m :
#                 a=m.index('-')
#                 c=float(m[a-1])-float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#     while ('+' in m) and ('-' in m) and (m.index('+'))>(m.index('-')):
#             if '-' in m :
#                 a=m.index('-')
#                 c=float(m[a-1])-float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#             elif '+' in m :
#                 a=m.index('+')
#                 c=float(m[a-1])+float(m[a+1])
#                 del m[a]
#                 del m[a]
#                 del m[a-1]
#                 m.insert(a-1,c)
#     while '-' in m :
#         a=m.index('-')
#         print(m)
#         c=float(m[a-1])-float(m[a+1])
#         del m[a]
#         del m[a]
#         del m[a-1]
#         m.insert(a-1,c)
#     while '+' in m :
#         a=m.index('+')
#         c=float(m[a-1])+float(m[a+1])
#         del m[a]
#         del m[a]
#         del m[a-1]
#         m.insert(a-1,c)

# print(m[0])
from tkinter import *




#Create a calculator class
class Calculator:




    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''
        
        #Assign reference to the main window of the application
        self.master = master

        #Add a name to our application
        master.title("Python Calculator")
        
        #Create a line where we display the equation
        self.equation=Entry(master, width=36, borderwidth=5)

        #Assign a position for the equation line in the grey application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Execute the .creteButton() method
        self.createButton()




    def createButton(self):

        '''
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        '''
        
        #We first create each button one by one with the value we want
        #Using addButton() method which is described below
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 =  self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')

        #Arrange the buttons into lists which represent calculator rows
        row1=[b7,b8,b9,b_add]
        row2=[b4,b5,b6,b_sub]
        row3=[b1,b2,b3,b_mult]
        row4=[b_clear,b0,b_equal,b_div]

        #Assign each button to a particular location on the GUI
        r=1
        for row in [row1, row2, row3, row4]:
            c=0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c+=1
            r+=1




    def addButton(self,value):

            '''
            DOCSTRING: Method to process the creation of a button and make it clickable
            INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
            OUTPUT: returns a designed button object
            '''
            return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))
    



    def clickButton(self, value):
        
        '''
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        '''
        
        #Get the equation that's entered by the user
        current_equation=str(self.equation.get())
        
        #If user clicked "c", then clear the screen
        if value == 'c':
            self.equation.delete(-1, END)
        
        #If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        
        #If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation+value)




#Execution
if __name__=='__main__':
    
    #Create the main window of an application
    root = Tk()
    
    #Tell our calculator class to use this window
    my_gui = Calculator(root)
    
    #Executable loop on the application, waits for user input
    root.mainloop()

