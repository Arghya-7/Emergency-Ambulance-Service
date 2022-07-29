from tkinter import *
import eas
userPincode=None
userLocation=None

def main():
    window=Tk()
    pinValue = IntVar()
    locValue = IntVar()
    def getPinAndLocations():
        global userLocation
        global userPincode
        userPincode=pinNumber.get()
        userLocation=locationname.get()
        if userPincode==None:
            userPincode=""
        if userLocation==None:
            userLocation=""
        user=eas.User(place=userLocation,pin=userPincode)
        window.destroy()
        if pinValue.get()==1:
            user.seePincodeWise()
        if locValue.get()==1:
            user.seeLocationWise()
        # call the ambulance service
    titlePage=Label(window,width=50,text="Emergency Ambulace Service",fg="Red",font=("Arial",20))
    titlePage.grid(row=0,column=0,columnspan=50)

    question1=Label(window,text="Enter your location name",font=("Arial",20))
    question1.grid(row=1,column=0)

    locationname=Entry(window,font=("Arial",20))
    locationname.grid(row=1,column=1)

    question2=Label(window,text="Enter your pin code",font=("Arial",20))
    question2.grid(row=2,column=0)

    pinNumber=Entry(window,font=("Arial",20))
    pinNumber.grid(row=2,column=1)
    # def checkLocValue():
    #     if locValue.get()==1:
    #         print("okk loc")
    #
    # def checkPinValue():
    #     if pinValue.get()==1:
    #         print("okk pin")

    checkBox1 = Checkbutton(window, text="Check pincode wise ambulace", font=("Arial", 15), onvalue=1, offvalue=0,
                            variable=pinValue)
    checkBox1.grid(row=3, column=0)
    checkBox2 = Checkbutton(window, text="Check location wise ambulace", font=("Arial", 15), onvalue=1, offvalue=0,
                            variable=locValue)
    checkBox2.grid(row=4, column=0)
    button1=Button(window,text="Submit",command=getPinAndLocations)
    button1.grid(row=5,column=48,columnspan=2)
    window.mainloop()
if __name__ == '__main__':
    main()