from tkinter import *
from tkinter import messagebox
import eas
driverAcitive=Tk()
driverAcitive.geometry("700x700")
def goOnline():
    pinCodeNumber = pincode.get()
    driverPhoneNumber=phoneNumber.get()
    driverLocation = loactionWiget.get()
    newDriver=eas.Driver(pinCodeNumber,driverLocation,driverPhoneNumber)
    newDriver.makeOnline()
    print(pinCodeNumber,driverPhoneNumber,driverLocation)

    messagebox.showinfo("Congratulation","You are ONLINE now")
    driverAcitive.destroy()
def goOffline():
    driverPhoneNumber=phoneNumber.get()
    newDriver=eas.Driver(None,None,driverPhoneNumber)
    print(newDriver.mobile)
    newDriver.makeOffline()
    messagebox.showinfo("Congratulation","You are OFFLINE now")
    driverAcitive.destroy()
welcomeWiget = Label(driverAcitive,text="Enter your credentials",font=("Arial",15,"bold"),fg="BLUE")
welcomeWiget.place(relx=0,rely=0.0,relheight=0.15,relwidth=0.8)


askPhoneNumber = Label(driverAcitive,text="Enter your 10 digit phone number:",font=("Arial"))
askPhoneNumber.place(relx=0,rely=0.15,relheight=0.1,relwidth=0.4)
phoneNumber = Entry(driverAcitive,font=("Arial",25,"bold","italic"),bd=5)
phoneNumber.place(relx=0.4,rely=0.15,relheight=0.1,relwidth=0.4)

askPin = Label(driverAcitive,text="Enter your pin-code number:",font=("Arial"))
askPin.place(relx=0,rely=0.3,relheight=0.1,relwidth=0.4)
pincode = Entry(driverAcitive,font=("Arial",25,"bold","italic"),bd=5)
pincode.place(relx=0.4,rely=0.3,relheight=0.1,relwidth=0.4)

askLoc = Label(driverAcitive,text="Enter your location name:",font=("Arial"))
askLoc.place(relx=0,rely=0.45,relheight=0.1,relwidth=0.4)
loactionWiget = Entry(driverAcitive,font=("Arial",25,"bold","italic"),bd=5)
loactionWiget.place(relx=0.4,rely=0.45,relheight=0.1,relwidth=0.4)

notice=Label(driverAcitive,text="Pin code, location is not required for going offline",fg="RED",font=("Arial"))
notice.place(relx=0.2,rely=0.6,relheight=0.1,relwidth=0.6)

goOnlineWiget = Button(text="Click here to go online",bg="GREEN",command=goOnline)
goOnlineWiget.place(relx=0.2,rely=0.75,relheight=0.2,relwidth=0.3)
goOnlineWiget.configure(font=("Arial"))

goOfflineWiget = Button(text="Click here to go offline",bg="RED",font=("Bold"),command=goOffline)
goOfflineWiget.place(relx=0.5,rely=0.75,relheight=0.2,relwidth=0.3)
driverAcitive.mainloop()