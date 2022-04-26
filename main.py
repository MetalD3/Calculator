

#importing modules
import math
from tkinter import *


#Setting up Window
root = Tk()
root.title("Calculator")

#Setting up number imput panel
e= Entry(root, width=35, borderwidth=5, )
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

#DEFINING FUNCTIONS OF THE +, -, *, /, = AND Clear BUTTONS  

#insertion function
def button_click(number):
    #e.delete(0, END)
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#clear
def button_cl():
    e.delete(0, END)

# + button
def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

# = button
def button_eq():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":

        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

# - button
def button_sub():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)



# * button
def button_mult():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


#divide button
def button_divid():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

















#Setting up buttons
button_1 = Button(root, text="1", padx=40, pady=20, borderwidth=5 ,command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=44, pady=20,borderwidth=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,borderwidth=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,borderwidth=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=44, pady=20,borderwidth=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,borderwidth=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,borderwidth=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=44, pady=20,borderwidth=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,borderwidth=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,borderwidth=5, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20,borderwidth=5, command=button_add)
button_minus = Button(root, text="-", padx=41, pady=20,borderwidth=5, command=button_sub)
button_mul = Button(root, text="x", padx=40, pady=20,borderwidth=5, command=button_mult)
button_div = Button(root, text="/", padx=45, pady=20,borderwidth=5, command=button_divid)

button_equal = Button(root, text="=", padx=91, pady=20,borderwidth=5, command=button_eq)
button_clear = Button(root, text="Clear", padx=82, pady=20,borderwidth=5, command=button_cl)




#placing buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_minus.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_mul.grid(row=6, column=2)


root.mainloop()
