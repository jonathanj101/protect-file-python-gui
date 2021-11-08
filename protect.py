import subprocess, os, platform
from tkinter import *
from tkinter import filedialog

##creating the main window and storing the window object in 'win'
win=Tk()
# setting the size of the window
win.geometry('400x200') 

def protect_path(user,password,filepath):
    user_input = input("username: ")
    password_input = input("password: ")

    if user == user_input and password==password_input:
        openfile = open(filepath,'r')
        print(openfile)
        print(platform.system())
        if platform.system() == "Linux":
            subprocess.call(('xdg-open',filepath))
    else:
        print("incorrect")

def get_filepath():
    filepath = filedialog.askopenfilename(initialdir="/media/jonathan/Storage/documents/Security/")
    print(filepath)
    protect_path("jon","jon", filepath)

def get_value():
    try:
        value = ent1.get()
        print(value)
    except ValueError:
        pass

label_name = Label(win,text='Name').grid(row=0)
label_email = Label(win,text="Email").grid(row=1)

btn = Button(text="Get Value", command=get_value).grid(column=2,row=2)
btn = Button(text="filepath", command=get_filepath).grid(column=1,row=3)


ent1 = Entry(win).grid(row=0,column=1)
ent2 = Entry(win).grid(row=1,column=1)

mainloop()
