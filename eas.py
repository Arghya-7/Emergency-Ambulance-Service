import sys
import mysql.connector
from tkinter import *
"""
Author : Arghya Dey
Date 07-03-2022
Place Kolkata
UserName :- Scott
Password :- Tiger
"""
# adminName = "Scott"
# adminPassword = "Tiger"

myHostDB="bnah2p0nvl3py94qhvvb-mysql.services.clever-cloud.com"
myUserDB="ua8ni9sphlltiyep"
myPasswordDb="vBpxVGhvR0ucMxE9vgkZ"
myDataBaseDb="bnah2p0nvl3py94qhvvb"

mydb=mysql.connector.connect(host =myHostDB,user=myUserDB,passwd=myPasswordDb,database=myDataBaseDb)

mycursor=mydb.cursor()

def showStatus():
    mycursor.execute("SELECT name,mobile,area,pincode  FROM service WHERE mode =" + "'" + str(1)+"'")
    result = mycursor.fetchall()
    userResultWindow = Tk()
    textLabel = f"{'Name':<12}{'Phone Number':>12}{'Area':>12}{'Pincode':>12}"
    textBar = Label(userResultWindow, text=textLabel, fg="Red").pack()
    for i in result:
        temp = f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}"
        resultOutput = Label(userResultWindow, text=temp).pack()
    userResultWindow.mainloop()
    mydb.commit()

#Service table
#mycursor.execute("CREATE TABLE service(name VARCHAR(255),mobile VARCHAR(20),area VARCHAR(255),mode VARCHAR(2))")

#Admin Table
#mycursor.execute("CREATE TABLE admin(mobile VARCHAR(20),password VARCHAR(20),PRIMARY KEY (mobile))")

class User:
    def __init__(self,place=None,pin=None):
        if place!=None:
            place=str(place).upper()
            self.place=place
        else:
            self.place=None
        if pin!=None:
            self.pin=str(pin)
        else:
            self.pin=None
    def usershowStatus(self):
        showStatus()

    def seeLocationWise(self):
        if self.place==None or self.pin==None:
            self.place = input("Enter the location name:").upper()
            self.pin = input("Enter the pincode without space:")
        try:
            sql = "SELECT name,mobile,area,pincode FROM service WHERE mode='1' AND area=" + "'" + self.place + "'" + " AND " "pincode=" + "'" + self.pin + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            userResultWindow = Tk()
            textLabel=f"{'Name':<12}{'Phone Number':>12}{'Area':>12}{'Pincode':>12}"
            textBar=Label(userResultWindow,text=textLabel,fg="Red").pack()
            for i in result:
                temp=f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}"
                resultOutput = Label(userResultWindow, text=temp).pack()
            userResultWindow.mainloop()


            # for i in result:
            #     print(f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}")
            mydb.commit()
        except Exception:
            print("Sorry no ambulance there")
            print("you can check by Pincode also")

    def seePincodeWise(self):
        if self.pin==None:
            self.pin = input("Enter the pincode without space:")
        try:
            sql = "SELECT name,mobile,area,pincode FROM service WHERE mode='1' AND pincode=" + "'" + self.pin + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            userResultWindow = Tk()
            textLabel=f"{'Name':<12}{'Phone Number':>12}{'Area':>12}{'Pincode':>12}"
            textBar=Label(userResultWindow,text=textLabel,fg="Red").pack()
            for i in result:
                temp=f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}"
                resultOutput = Label(userResultWindow, text=temp).pack()
            userResultWindow.mainloop()


            # for i in result:
            #     print(f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}")
            mydb.commit()
            mydb.commit()
        except Exception:
            print("Sorry no ambulance there")
            print("you can check by Pincode also")

    def control(self):
        try:
            print("*****Welcome User******")
            print("1 for available Ambulance of database")
            print("2 for check Location and pin wise Ambulance")
            print("3 for pincode wise ambulance")
            ch=int(input("Enter your choice:"))
            if ch==1:
                self.usershowStatus()
            elif ch==2:
                self.seeLocationWise()
            elif ch==3:
                self.seePincodeWise()
            else:
                print("Wrong choice")
        except Exception:
            print("Follow the instructions")
            if type(self)==User:
                self.control()


class Driver:
    def __init__(self,pincode=None,location=None,mobile=None,name=None) -> None:
        self.name=name
        self.pincode=pincode
        self.location=location
        self.mobile=mobile
    def add(self):
        try:
            if self.name !=None:
                name = self.name
            else:
                name=input("Enter your name:").upper()
                self.name = name
            if self.mobile!=None:
                mobile=self.mobile
            else:
                while True:
                    mobile = input("Enter 10 digit mobile number:")
                    if len(mobile) != 10:
                        print("Oops!Your mobile number is not 10 digit")
                    else:
                        break
                self.mobile=mobile
            if self.location != None:
                area = self.location
            else:
                area=input("Enter the area:").upper()
                self.location = area
            mode="0"
            if self.pincode!=None:
                pincode=self.pincode
            else:
                pincode = input("Enter the pincode:")
                self.pincode=pincode
            print(name,mobile,area,pincode)
            sql="INSERT INTO service(name ,mobile,area,mode,pincode) VALUES(%s,%s,%s,%s,%s);"
            val=(name,mobile,area,mode,pincode)
            mycursor.execute(sql,val)
            mydb.commit()
        except Exception:
            print("You are already registered or some internal issue occurs")
            print("Contact admin")
    def deleteRecord(self):
        mobile = input("Enter 10 digit mobile number:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
        mydb.commit()
    def driverShowStatus(self):
        showStatus()

    def makeOffline(self):
        if self.mobile==None:
            mobile = input("Enter 10 digit mobile number of the Driver:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
            self.mobile=mobile
        else:
            mobile=self.mobile
        sql="UPDATE service SET mode=" + "'" + str(0) + "'"  + "WHERE mobile="+ "'" + mobile + "';"
        mycursor.execute(sql)
        mydb.commit()

    def makeOnline(self):
        mobile=None
        if self.mobile==None:
            mobile = input("Enter 10 digit mobile number of the Driver:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
        if self.mobile==None:
            self.mobile=mobile
        if mobile==None:
            mobile=self.mobile
        self.changeLocation(mobile)
        sql="UPDATE service SET mode=" + "'" + str(1) +"'" + "WHERE mobile="+ "'" + mobile + "'"
        mycursor.execute(sql)
        mydb.commit()

    def changeLocation(self,mobile=None,place=None,pincode=None):
        if self.mobile==None:
            mobile=self.mobile
        elif mobile==None:
            mobile = input("Enter 10 digit mobile number of the Driver:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
            self.mobile=mobile
        if self.location!=None:
            place = self.location.upper()
        else:
            place = input("Enter the location:").upper()
            self.location=place

        if self.pincode!=None:
            pincode=self.pincode
        else:
            pincode = input("Enter the pin:")
            self.pincode=pincode
        sql = "UPDATE service SET area='" + place + "', pincode='" + pincode + "'" + " WHERE mobile=" + "'" + mobile + "'"
        mycursor.execute(sql)
        mydb.commit()


    def selfVisualization(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        sql = "SELECT name,mobile,area,pincode FROM service WHERE mobile='" + mobile + "'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(f"{'Name':<12}{'Phone Number':>12}{'Area':>12}{'Pincode':>12}")
        for i in result:
            print(f"{i[0]:<12}{i[1]:>12}{i[2]:>12}{i[3]:>12}")

    def control(self):
        try:
            print("*****Welcome Driver******")
            print("1 for Sign-up in database")
            print("2 delete your record permanently")
            print("3 for showing available drivers in database")
            print("4 for going offline")
            print("5 for going online")
            print("6 for change location")
            print("7 for checking personal details")
            ch=int(input("Enter the choice:"))
            if ch == 1:
                self.add()
            elif ch==2:
                self.deleteRecord()
            elif ch==3:
                self.driverShowStatus()
            elif ch==4:
                self.makeOffline()
            elif ch==5:
                self.makeOnline()
            elif ch==6:
                self.changeLocation()
            elif ch==7:
                self.selfVisualization()
            else:
                print("Wrong choice")
        except Exception:
            print("Follow the instructions")
            if type(self)==Driver:
                self.control()
class Creator(Driver,User):
    def redefineDatabase(self):
        #mycursor.execute("DROP TABLE service")
        mycursor.execute("DROP TABLE IF EXISTS service")
        mycursor.execute("CREATE TABLE service(name VARCHAR(255),mobile VARCHAR(20),area VARCHAR(255),mode VARCHAR(2),pincode VARCHAR(225),PRIMARY KEY (mobile))")
        mydb.commit()
    def creatorShowStatus(self):
        showStatus()

    def add(self):
        try:
            name=input("Enter driver name:").upper()
            while True:
                mobile = input("Enter 10 digit mobile number:")
                if len(mobile) != 10:
                    print("Re-Enter Mobile number")
                else:
                    break
            area=input("Enter the area:").upper()
            mode="0"
            pincode = input("Enter the pincode:")
            sql="INSERT INTO service(name ,mobile,area,mode,pincode) VALUES(%s,%s,%s,%s,%s);"
            val=(name,mobile,area,mode,pincode)
            mycursor.execute(sql,val)
            mydb.commit()
        except Exception:
            print("You are already registered or some internal issue occurs")
            print("Contact admin")

    def delete(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
        mydb.commit()

    def showFullDatabase(self):
        mycursor.execute("SELECT * FROM service")
        result = mycursor.fetchall()
        for i in result:
            print(i)
        mydb.commit()

    def findDriver(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        try:
            sql = "SELECT * FROM service WHERE mobile='" + mobile + "';"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            if len(result) == 0:
                print("No data found")
            else:
                for i in result:
                    print(i)
        except Exception:
            pass

    def insertIntoAdminTable(self):
        mobile = input("Enter 10 digit mobile number of the Admin:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break

        password = "123"
        sql = "INSERT INTO admin(mobile,password) VALUES (%s,%s)"
        val = (mobile, password)
        mycursor.execute(sql, val)
        mydb.commit()

    def checkPassword(self,mobile=None,password=None):
        if mobile==None or password==None:
            mobile = input("Enter 10 digit mobile number of the Admin:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
            password = input("Enter your password:")
        sql = "SELECT * FROM admin WHERE mobile = '" + mobile + "' AND password='" + password + "'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if len(result) == 0:
            print("Mistakes occur in Phone number or Password")
            return False
        else:
            return True

    def updateAdminPassword(self):
        mobile = input("Enter 10 digit mobile number of the Admin:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        oldPassword = input("Enter old password:")
        newPassword = input("Enter new Password:")
        if self.checkPassword(mobile,oldPassword) is True:
            sql = "UPDATE admin SET password = '" + newPassword + "' " + "WHERE mobile='" + mobile + "' AND password='" + oldPassword + "'"
            mycursor.execute(sql)
            mydb.commit()

    def deleteAdmin(self):
        mobile = input("Enter 10 digit mobile number of the Admin:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        password = input("Enter your password:")
        sql = "DELETE FROM admin WHERE mobile='" + mobile + "' AND password='" + password + "'"
        mycursor.execute(sql)
        mydb.commit()
    def changeAdminStatusToActive(self,mobile=None,password=None):
        if mobile==None and password==None:
            mobile = input("Enter 10 digit mobile number of the Admin:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
            password = input("Enter your password:")
        sql="UPDATE admin SET mode='1' WHERE mobile='" + mobile + "'"
        mycursor.execute(sql)
        mydb.commit()
    def changeAdminStatusToInactive(self,mobile=None,password=None):
        if mobile==None and password==None:
            mobile = input("Enter 10 digit mobile number of the Admin:")
            while True:
                if len(mobile) != 10:
                    mobile = input("Re-enter mobile number:")
                else:
                    break
            password = input("Enter your password:")
        sql="UPDATE admin SET mode='0' WHERE mobile='" + mobile + "'"
        mycursor.execute(sql)
        mydb.commit()
    def showActiveAdminTable(self):
        mycursor.execute("SELECT * FROM admin WHERE mode='1'")
        result = mycursor.fetchall()
        for i in result:
            print(i)
    def showAdminTable(self):
        mycursor.execute("SELECT * FROM admin")
        result = mycursor.fetchall()
        for i in result:
            print(i)
    def control(self):
        try:
            while True:
                print("0 for exit")
                print("1 for Redefine Database")
                print("2 for seeing Full Database")
                print("3 for making  sign-in a driver")
                print("4 for delete particular driver records")
                print("5 to find a driver")
                print("6 for getting Driver-Class-Control")
                print("7 for getting User-Class-Control")
                print("8 for insert a person into admin table")
                print("9 for change admin password")
                print("10 for delete admin")
                print("11 for showing admin table")
                print("12 for showing active admin table")
                ch=int(input("Enter the choice:"))
                if ch==0:
                    break
                if ch==1:
                    self.redefineDatabase()
                elif ch==2:
                    self.showFullDatabase()
                elif ch==3:
                    self.add()
                elif ch==4:
                    self.delete()
                elif ch==5:
                    self.findDriver()
                elif ch==6:
                    Driver.control(self)
                elif ch==7:
                    User.control(self)
                elif ch==8:
                    self.insertIntoAdminTable()
                elif ch==9:
                    self.updateAdminPassword()
                elif ch==10:
                    self.deleteAdmin()
                elif ch==11:
                    self.showAdminTable()
                elif ch==12:
                    self.showActiveAdminTable()
                else:
                    print("You have entered wrong choice")
        except Exception:
            print("Follow the instructions")
            if type(self)==Creator:
                self.control()


def main():
    print("1 for Creator")
    print("2 for User")
    print("3 for Drivers")
    ch=int(input("Enter the choice:"))
    if ch == 1:
        mobile = input("Enter 10 digit mobile number of the Admin:")
        while True:
            if len(mobile) != 10:
                mobile = input("Re-enter mobile number:")
            else:
                break
        password=input("Enter the password:")
        obj1=Creator()
        if obj1.checkPassword(mobile,password) is True:
            print("Welcome Admin")
            obj = Creator()
            obj.changeAdminStatusToActive(mobile,password)
            obj.control()
            obj.changeAdminStatusToInactive(mobile,password)
            sys.exit(0)
    elif ch == 2:
        obj= User()
        obj.control()
    elif ch == 3:
        obj = Driver()
        obj.control()
    else:
        print("You entered wrong choice")
if __name__== "__main__" :
    main()
mydb.commit()