from tkinter import *

##creating the main window and storing the window object in 'win'
win=Tk()
# setting the size of the window
win.geometry('400x200') 

Label(win,text="Name").grid(row=0)
Label(win,text="Email").grid(row=1)

ent1 = Entry(win)
ent2 = Entry(win)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)

mainloop()
