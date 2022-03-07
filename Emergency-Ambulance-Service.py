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
    mycursor.execute("SELECT *  FROM service")
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
        mycursor.execute("CREATE TABLE service(name VARCHAR(255),mobile VARCHAR(20),area VARCHAR(255),mode VARCHAR(2))")
    def creatorShowStatus(self):
        showStatus()
    def add(self):
        name=input("Enter driver name:").upper()
        while True:
            mobile = input("Enter 10 digit mobile number:")
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        area=input("Enter the area:").upper()
        mode="1"
        sql="INSERT INTO service(name ,mobile,area,mode) VALUES(%s,%s,%s,%s);"
        val=(name,mobile,area,mode)
        mycursor.execute(sql,val)
    def offline(self):
        mobile = input("Enter 10 digit mobile number of the Driver:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
    def control(self):
        while True:
            print("0 for exit")
            print("1 for Redefine Database")
            print("2 for seeing Status")
            print("3 for add a driver")
            print("4 for delete particular driver")
            ch=int(input("Enter the choice:"))
            if ch==0:
                break
            if ch==1:
                self.redefineDatabase();
            elif ch==2:
                self.creatorShowStatus()
            elif ch==3:
                self.add()
            elif ch==4:
                pass
            else:
                print("You have entered wrong choice")

class User:
    def usershowStatus(self):
        showStatus()
    def control(self):
        print("1 for seeing whole database")
        ch=int(input("Enter your choice:"))
        if ch==1:
            self.usershowStatus()
class Driver:
    def add(self):
        name=input("Enter Your name:").upper()
        while True:
            mobile = input("Enter 10 digit mobile number:")
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        area=input("Enter the area:").upper()
        mode="1"
        sql="INSERT INTO service(name ,mobile,area,mode) VALUES(%s,%s,%s,%s);"
        val=(name,mobile,area,mode)
        mycursor.execute(sql,val)
    def offline(self):
        mobile = input("Enter 10 digit mobile number:")
        while True:
            if len(mobile) != 10:
                print("Re-Enter Mobile number")
            else:
                break
        sql="DELETE FROM service WHERE mobile= " + "'"+ mobile + "'"
        mycursor.execute(sql)
    def driverShowStatus(self):
        showStatus()
    def control(self):
        print("1 for adding to you in database")
        print("2 for if you are going offline")
        print("3 for showing full database")
        ch=int(input("Enter the choice:"))
        if ch==1:
            self.add()
        elif ch==2:
            self.offline()
        elif ch==3:
            self.driverShowStatus()
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