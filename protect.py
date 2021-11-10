import subprocess, os, platform
from tkinter import *
from tkinter import filedialog

##creating the main window and storing the window object in 'win'
win=Tk()
# setting the size of the window
win.geometry('400x200') 

def check_system_platform(filepath):
    if platform.system() == "Darwin":
        subprocess.call(('open',filepath))
    elif platform.system == "Windows":
        os.startfile(filepath)
    else:
        subprocess.call(('xdg-open',filepath))

def protect_path(user,password,filepath):
    user_input = input("username: ")
    password_input = input("password: ")

    if user == user_input and password==password_input:
        check_system_platform(filepath)
    else:
        print("incorrect password")

def get_filepath():
    filepath = filedialog.askopenfilename(initialdir="/media/jonathan/Storage/documents/Security/")
    print(filepath)
    protect_path("jon","jon", filepath)

# def get_value():
#     try:
#         value = ent1.get()
#         print(value)
#     except ValueError:
#         pass
# filepath label
# filepath_label = Label(win,text='Name').grid(row=0)
# Display an input to add text..
# filepath_entry = Entry(win).grid(row=0,column=1)

btn = Button(text="filepath", command=get_filepath).grid(column=1,row=3)


mainloop()
