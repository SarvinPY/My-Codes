from tkinter import *
# def print_my_name () :
#     print('my name is mohammad') 
root = Tk()
root.title('button')
root.geometry('400x300')
root.resizable(width=FALSE , height=False)
input_name = Entry(root)
input_name.place(x = 10 , y = 35)
header = Label(root , text='Enter your name: ' )
header.place(x = 10 , y = 10)
btn =Button(root , text='Enter')
btn.place(x = 40 , y = 70)
def get_name () :
    print(input_name.get())
root.mainloop()