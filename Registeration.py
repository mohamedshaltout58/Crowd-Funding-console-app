import re                #import regix
from userid import *     #import userid.py file
def registeration(): #registeration with argument of the id which given from userid.py
    #Mobile vaidation
    def checkmobile(mobile):
        mob = r'01[0-9]{9}$'
        if re.match(mob, mobile):
            return True
        else:
            return False
    #Mail validation
    def checkemail(mail):
        email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(email, mail):
            return True
        else:
            return False
    #Name validation
    def checkname(x):
        if ((not x.isspace()) and (x.isalpha())):
            validname = x
            return True
        else:
            return False
    #password validation
    def passwordmatch(p1, p2):
        if p1 == p2:
            return True
        else:
            return False

    while True:
        Firstname = input("Please , Enter Your First Name : \n ")
        if checkname(Firstname) == True:
            fname = Firstname.capitalize()
        else:
            print("WRONG ENTRY !!! Please , Enter a valid name")
            continue
        while True:
            Lastname = input("Please Enter Your Last Name : ")
            if checkname(Lastname) == True:
                lname = Lastname.capitalize()
                break
            else:
                print("WRONG ENTRY !!! Please , Enter a Valid Name")
                continue
        while True:
            Mail = input("Please , Enter Your E-mail : ")
            if checkemail(Mail) == True:
                mail = Mail
                break
            else:
                print("WRONG ENTRY !!! Please , Enter A Valid Email Address !")
                continue
        while True:
            password = input("Please , Enter Your Password :")
            confirmpassword = input("Please , Enter Your Password Again  :")
            if passwordmatch(password, confirmpassword) == True:
                passwd = password
                break
            else:
                print("WRONG MATCHING PASSWORDS !!!")
                continue
        while True:
            Mobile = input("Please Enter Your Mobile Number : ")
            if checkmobile(Mobile) == True:
                mob = Mobile
                break
            else:
                print("Wrong Mobile Number!!!")
                continue
        break

    try:
        fileobject = open("userinfo.txt", "a")
    except Exception as e:
        print(e)
    else:
        userinfo = f"{userid()}:{fname}:{lname}:{mail}:{passwd}:{mob}\n"
        print(userinfo)
        fileobject.write(userinfo)
        fileobject.close()