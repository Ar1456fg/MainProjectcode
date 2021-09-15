#Admission system
#must use gui to guage options and options should vary depending on course chosen
#take name as input and print it saying welcome and finally display a message with all their chosen course and image
from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title('harvard university campus web')
frame = Frame(window)
entry = Entry(frame)
def dialog3():
        box.showinfo('selection', 'Your choice:' + \
        listbox.get(listbox.curselection()))

def dialog2():
    var = box.askyesno('important notice', 'Are you on a scholarship?')
    if var == 1:
        window2 = Tk()
        window2.title('course selection')
        frame2 = Frame(window2)
        global listbox
        listbox = Listbox(frame2)
        listbox.insert(1, 'Arts')
        listbox.insert(2, 'Science')
        listbox.insert(3, 'commerce')
        btn2 = Button(frame2, text = 'choose', command = dialog3)
        btn2.pack( side = RIGHT, padx = 5)
        listbox.pack( side = LEFT)
        frame2.pack(padx = 30, pady = 30)
        windows.mainloop()
    else:
        box.showinfo('No box', 'cancelling..')
        window2 = Tk()
        window2.title('course selection')
        frame2 = Frame(window2)
        listbox = Listbox(frame2)
        listbox.insert(1, 'Science')
        listbox.insert(2, 'commerce')
        btn2 = Button(frame2, text = 'choose', command = dialog3)
        btn2.pack( side = RIGHT, padx = 5)
        listbox.pack( side = LEFT)
        frame2.pack(padx = 30, pady = 30)
        windows.mainloop()

def dialog():
    box.showinfo('Greetings' , 'Welcome ' + entry.get())
    dialog2()

btn = Button(frame, text = 'Enter student name' ,command = dialog)
btn.pack( side = RIGHT, padx = 5)
entry.pack( side = LEFT)
frame.pack(padx = 20, pady = 20)
window.mainloop()
