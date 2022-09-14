from tkinter import *
import os
import subprocess
driverReg = Tk()
driverReg.geometry("700x700")
def generate():
    option=radiobutton_variable.get()
    if option==1:
        print("It is registration")
    elif option==2:
        print("It is login")
        subprocess.Popen("DriverLogin.py 1", shell=True)
    elif option==3:
        print("others")
    else:
        print(radiobutton_variable)
    driverReg.destroy()
header = Label(driverReg,text="You have logged-in as a Driver",font=("Arial",15,"bold","italic"),bg="blue",fg="red")
header.place(relx=0.2,rely=0,relheight=0.2,relwidth=0.6)

radiobutton_variable = IntVar()
registrationWiget=Radiobutton(driverReg, text="Click here for registration", variable = radiobutton_variable, value = 1)
registrationWiget.place(relx=0.1,rely=0.25,relheight=0.1,relwidth=0.8)
loginWiget=Radiobutton(driverReg, text="Click here for login",  variable = radiobutton_variable, value = 2)
loginWiget.place(relx=0.0725,rely=0.35,relheight=0.1,relwidth=0.8)
othersWiget=Radiobutton(driverReg, text="Click here to see other information",  variable = radiobutton_variable, value = 3)
othersWiget.place(relx=0.1,rely=0.45,relheight=0.1,relwidth=0.8)

checkBox = Button(driverReg,text="Submit",bg="RED",font=("Bold"),command=generate)
checkBox.place(relx=0.4,rely=0.65,relheight=0.15,relwidth=0.15)
driverReg.mainloop()