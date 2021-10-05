#GUI PROGRAMMING
'''from tkinter import *
root = Tk()
mylabel = Label(root, text="Hello world!").grid(row = 0, column = 0)
mylabel2 = Label(root, text="My name is Aryan!")
mylabel3 = Label(root, text="indication")
mylabel2.grid(row = 20, column = 20)
mylabel3.grid(row = 25, column = 25)
root.mainloop()'''
#Buttons
'''from tkinter import *
root = Tk()
def myclick():
    mylabel = Label(root, text = "Confirmed!")
    mylabel.pack()
    myButton = Button(root, text = "Click Me!",padx = 50, pady = 50, command = myclick, fg = "yellow",bg = "blue", state = DISABLED)
    myButton.pack()
myButton = Button(root, text = "Click Me!",padx = 50, pady = 50, command = myclick, fg = "yellow",bg = "blue")
myButton.pack()
root.mainloop()'''
#INput boxes and entry widgets
'''from tkinter import *
root = Tk()
def function():
    input1.insert(0, "Enter Your name:")
entrybutton = Button(root, text = "Enter name", bg = "cyan", command = function).grid(row = 0, column = 1)
input1 = Entry(root, width = 50, bg = "yellow", fg = "green", borderwidth = 5).grid(row = 0, column = 0)
#input1.grid(row = 0, column = 0)
#input1.insert(0, "Enter Your name:")
root.mainloop()
#Building a caluclator'''
from tkinter import *
root = Tk()
root.title("calculator")
def function(x):
    input1.insert(0, str(x))

def clear():
    input1.delete(0, END)

def calculate():
    z = input1.get()
    p = 0
    x = ""
    for i in z:
        p = p + 1
        try:
            y = int(i)
            x = x + i
        except ValueError:
            if i == 'x':
                g = len(z)
                n = z[p:g]
                input1.delete(0, END)
                input1.insert(0, str(int(n) * int(x)))
            elif i == '-':
                g = len(z)
                n = z[p:g]
                input1.delete(0, END)
                input1.insert(0, str(int(n) - int(x)))
            elif i == '/':
                g = len(z)
                n = z[p:g]
                input1.delete(0, END)
                input1.insert(0, str(int(n) / int(x)))
            elif i == '+':
                g = len(z)
                n = z[p:g]
                input1.delete(0, END)
                input1.insert(0, str(int(n) + int(x)))
            else:
                input1.delete(0, END)
                input1.insert(0, "Syntax ERROR")
btn1 = Button(root, text = "1", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(1)).grid(row = 1, column = 1)
btn2 = Button(root, text = "2", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(2)).grid(row = 1, column = 2)
btn3 = Button(root, text = "3", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(3)).grid(row = 1, column = 3)
btn4 = Button(root, text = "4", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(4)).grid(row = 2, column = 1)
btn5 = Button(root, text = "5", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(5)).grid(row = 2, column = 2)
btn6 = Button(root, text = "6", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(6)).grid(row = 2, column = 3)
btn7 = Button(root, text = "7", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(7)).grid(row = 3, column = 1)
btn8 = Button(root, text = "8", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(8)).grid(row = 3, column = 2)
btn9 = Button(root, text = "9", padx = 40, pady = 40,bg = 'cyan', command = lambda: function(9)).grid(row = 3, column = 3)
equal = Button(root, text = "=", padx = 40, pady = 40,bg = 'cyan', command = calculate).grid(row = 1, column = 4)
addition = Button(root, text = "+", padx = 40, pady = 40,bg = 'cyan', command = lambda: function("+")).grid(row = 2, column = 4)
multiply = Button(root, text = "x", padx = 40, pady = 40,bg = 'cyan', command = lambda: function("x")).grid(row = 3, column = 4)
minus = Button(root, text = "-", padx = 40, pady = 40,bg = 'cyan', command = lambda: function("-")).grid(row = 1, column = 5)
divide = Button(root, text = "/", padx = 40, pady = 40,bg = 'cyan', command = lambda: function("/")).grid(row = 2, column = 5)
clear = Button(root, text = "clear", padx = 30, pady = 40,bg = 'cyan', command = clear).grid(row = 3, column = 5)
input1 = Entry(root, width = 78, bg = "yellow", borderwidth = 5)
input1.grid(row = 0, column = 0, columnspan = 6)
root.mainloop()
