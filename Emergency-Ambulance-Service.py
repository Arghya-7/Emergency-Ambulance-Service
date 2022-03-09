import sys
import mysql.connector
"""
Author : Arghya Dey
Date 07-03-2022
Place Kolkata

UserName :- Scott
Password :- Tiger
"""
adminName = "Scott"
adminPassword = "Tiger"

myHostDB="bnah2p0nvl3py94qhvvb-mysql.services.clever-cloud.com"
myUserDB="ua8ni9sphlltiyep"
myPasswordDb="vBpxVGhvR0ucMxE9vgkZ"
myDataBaseDb="bnah2p0nvl3py94qhvvb"

mydb=mysql.connector.connect(host =myHostDB,user=myUserDB,passwd=myPasswordDb,database=myDataBaseDb)

mycursor=mydb.cursor()

def showStatus():
    mycursor.execute("SELECT *  FROM service WHERE mode =" + "'" + str(1)+"'")
    result = mycursor.fetchall()
    for i in result:
        print(i)

#mycursor.execute("CREATE TABLE service(name VARCHAR(255),mobile VARCHAR(20),area VARCHAR(255),mode VARCHAR(2))")

#sql="INSERT INTO service(name ,mobile,area,mode) VALUES(%s,%s,%s,%s);"
#val=("Ram","6290103454","purbachal","1")
#mycursor.execute(sql,val)
class Creator:
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
            mode="1"
            pincode = input("Enter the pincode:")
            sql="INSERT INTO service(name ,mobile,area,mode,pincode) VALUES(%s,%s,%s,%s,%s);"
            val=(name,mobile,area,mode,pincode)
            mycursor.execute(sql,val)
            mydb.commit()
        except Exception:
            print("You are already registered or some internal issue occurs")
            print("Contact admin")

    def offline(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
        mydb.commit()

    def tempBreak(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="UPDATE service SET mode=" + "'" + str(0) +"'" + "WHERE mobile="+ "'" + mobile + "';"
        mycursor.execute(sql)
        mydb.commit()

    def afterBreak(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="UPDATE service SET mode=" + "'" + str(1) +"'" + "WHERE mobile="+ "'" + mobile + "'"
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
                print("Re-Enter Mobile number")
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

    def control(self):
        while True:
            print("0 for exit")
            print("1 for Redefine Database")
            print("2 for seeing Full Database")
            print("3 for add a driver")
            print("5 for delete particular driver")
            print("6 for temporary break")
            print("7 for after returning from break")
            print("8 to find drivers")
            ch=int(input("Enter the choice:"))
            if ch==0:
                break
            if ch==1:
                self.redefineDatabase()
            elif ch==2:
                self.showFullDatabase()
            elif ch==3:
                self.add()
            elif ch==5:
                self.offline()
            elif ch==6:
                self.tempBreak()
            elif ch==7:
                self.afterBreak()
            elif ch==8:
                self.findDriver()
            else:
                print("You have entered wrong choice")

class User:
    def usershowStatus(self):
        showStatus()

    def seeLocationWise(self):
        place = input("Enter the location name:").upper()
        pin = input("Enter the pincode without space:")
        try:
            sql = "SELECT * FROM service WHERE area=" + "'" + place + "'" + " AND " "pincode=" + "'" + pin + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in result:
                print(i)
        except Exception:
            print("Sorry no ambulance there")
            print("you can check by Pincode also")
    def seePincodeWise(self):
        pin = input("Enter the pincode without space:")
        try:
            sql = "SELECT * FROM service WHERE pincode=" + "'" + pin + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in result:
                print(i)
        except Exception:
            print("Sorry no ambulance there")
            print("you can check by Pincode also")
    def control(self):
        print("1 for available Ambulance of database")
        print("2 for check Location and pin wise Ambulance")
        print("3 for pincode ambulance")
        ch=int(input("Enter your choice:"))
        if ch==1:
            self.usershowStatus()
        elif ch==2:
            self.seeLocationWise()
        elif ch==3:
            self.seePincodeWise()
        else:
            print("Wrong choice")
class Driver:
    def add(self):
        try:
            name=input("Enter your name:").upper()
            while True:
                mobile = input("Enter 10 digit mobile number:")
                if len(mobile) != 10:
                    print("Re-Enter Mobile number")
                else:
                    break
            area=input("Enter the area:").upper()
            mode="1"
            pincode = input("Enter the pincode:")
            sql="INSERT INTO service(name ,mobile,area,mode,pincode) VALUES(%s,%s,%s,%s,%s);"
            val=(name,mobile,area,mode,pincode)
            mycursor.execute(sql,val)
            mydb.commit()
        except Exception:
            print("You are already registered or some internal issue occurs")
            print("Contact admin")
    def offline(self):
        mobile = input("Enter 10 digit mobile number:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
        mydb.commit()
    def driverShowStatus(self):
        showStatus()
    def tempBreak(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="UPDATE service SET mode=" + "'" + str(0) +"'" + "WHERE mobile="+ "'" + mobile + "';"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
    def afterBreak(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="UPDATE service SET mode=" + "'" + str(1) +"'" + "WHERE mobile="+ "'" + mobile + "'"
        mycursor.execute(sql)
        mydb.commit()
    def control(self):
        print("1 for adding to you in database")
        print("2 for if you are going offline")
        print("3 for showing available drivers in database")
        print("4 for temporary break")
        print("5 for after return from temporary break")
        ch=int(input("Enter the choice:"))
        if ch == 1:
            self.add()
        elif ch==2:
            self.offline()
        elif ch==3:
            self.driverShowStatus()
        elif ch==4:
            self.tempBreak()
        elif ch==5:
            self.afterBreak()
def main():
    print("1 for Creator")
    print("2 for User")
    print("3 for Drivers")
    ch=int(input("Enter the choice:"))
    if ch == 1:
        name=input("Enter the Username:")
        password=input("Enter the password:")
        if name== adminName and password==adminPassword:
            print("Welcome Admin")
            obj = Creator()
            obj.control()
        else:
            print("Oops!You Have Entered Wrong Password")
            print("Please Login Again")
            sys.exit(0)
    elif ch == 2:
        obj= User()
        obj.control()
    elif ch == 3:
        obj = Driver()
        obj.control()
if __name__== "__main__" :
    main()
mydb.commit()