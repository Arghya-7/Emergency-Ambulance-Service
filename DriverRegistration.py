from tkinter import *
from tkinter import messagebox
import eas
registration = Tk()
registration.geometry("700x700")
def generate():
    location=loactionWiget.get().upper()
    mobile=phoneNumber.get()
    if len(mobile)==10:
        pincodeNumber=pincode.get()
        name=driverName.get().upper()
        newDriver = eas.Driver(location,pincodeNumber,mobile,name)
        newDriver.add()
        # print(newDriver.pincode,newDriver.location,newDriver.name,newDriver.mobile)
        # print(location,mobile,pincodeNumber,name)
    else:
        messagebox.showinfo("Oops","Mobile number should be 10 digit")
welcomeWiget = Label(registration,text="Enter your credentials",font=("Arial",15,"bold"),fg="BLUE")
welcomeWiget.place(relx=0,rely=0.0,relheight=0.15,relwidth=0.8)


askPhoneNumber = Label(registration,text="Enter your 10 digit phone number:",font=("Arial"))
askPhoneNumber.place(relx=0,rely=0.15,relheight=0.1,relwidth=0.4)
phoneNumber = Entry(registration,font=("Arial",25,"bold","italic"),bd=5)
phoneNumber.place(relx=0.4,rely=0.15,relheight=0.1,relwidth=0.4)

askPin = Label(registration,text="Enter your pin-code number:",font=("Arial"))
askPin.place(relx=0,rely=0.3,relheight=0.1,relwidth=0.4)
pincode = Entry(registration,font=("Arial",25,"bold","italic"),bd=5)
pincode.place(relx=0.4,rely=0.3,relheight=0.1,relwidth=0.4)

askLoc = Label(registration,text="Enter your location name:",font=("Arial"))
askLoc.place(relx=0,rely=0.45,relheight=0.1,relwidth=0.4)
loactionWiget = Entry(registration,font=("Arial",25,"bold","italic"),bd=5)
loactionWiget.place(relx=0.4,rely=0.45,relheight=0.1,relwidth=0.4)

askName = Label(registration,text="Enter your name:",font=("Arial"))
askName.place(relx=0,rely=0.6,relheight=0.1,relwidth=0.4)
driverName = Entry(registration,font=("Arial",25,"bold","italic"),bd=5)
driverName.place(relx=0.4,rely=0.6,relheight=0.1,relwidth=0.4)

checkBox = Button(registration,text="Submit",bg="RED",font=("Bold"),command=generate)
checkBox.place(relx=0.4,rely=0.75,relheight=0.1,relwidth=0.1)
registration.mainloop()