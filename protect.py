import subprocess, os, platform, psutil
from tkinter import *
from tkinter import filedialog


##creating the main window and storing the window object in 'win'
win=Tk()
# setting the size of the window
win.geometry('400x200') 
# looping through system processes
# for i in psutil.process_iter():
#     # checking if file is open, have to dive deeper about soffice in linux and others os process name for file
#     if i.name() == "soffice.bin":
#         # terminating process
#         i.terminate()
# nemo (linux file explorer), 
# evince for pdf file viewer (?, might be right need to invistigate), 
# oosplash (in charge to open files like .odt)
    
def user_auth():
    username_label = Label(win,text='username')
    password_label = Label(win,text="password")

    username_label_entry = Entry(win)

    username_value = username_label_entry.get()

    print(username_label_entry)


def check_system_platform(filepath):
    if platform.system() == "Darwin":
        subprocess.call(('open',filepath))
    elif platform.system == "Windows":
        os.startfile(filepath)
    else:
        subprocess.call(('xdg-open',filepath))

# def protect_path(user,password,filepath):
    # user_input = input("username: ")
    # password_input = input("password: ")

    # if user == user_input and password==password_input:
    #     check_system_platform(filepath)
    # else:
    #     print("incorrect password")

def get_filepath():
    filepath = filedialog.askopenfilename(initialdir="/media/jonathan/Storage/documents/Security/")
    print(filepath)
    # protect_path("jon","jon", filepath)

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
