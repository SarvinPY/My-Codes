from tkinter import *
# def print_my_name () :
#     print('my name is mohammad') 
root = Tk()
root.title('button')
root.geometry('400x300')
root.resizable(width=FALSE , height=False)
full_name = StringVar()
def print_my_name () :
    full_name.set('my name is mohammad')
btn = Button(root , text='click me !' , command= lambda : print_my_name())
btn.place(x = 170 , y = 120)
label = Label(root , textvariable = full_name)
label.place(x = 10, y = 30)
root.mainloop()
