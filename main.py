#this is the launching page of Crowd-Funding console app
from Registeration import registeration   #import the registeration function
from Login import login                  #import the login function
def launchapp():                        #app main menu a function to start app
    while True:
        welcome_massage = "Welcome to Crowd funding application"
        print(welcome_massage.center(100, "="))
        print(
            "HINT : \nIf this is your first time , please choose (1) register now. \nIf you are a member already ,Please choose (2) Login")
        print("(1) Register now. \n(2) Login. \n(3) Exit")

        userchoice = input("==> ")
        if userchoice == "1" :              #open registeration function and then return to this script to login
            registeration()
        elif userchoice == "2" :            #enable loginfunction and continue in the app with it and break the true loop after finishing
            login()
            break
        elif userchoice == "3" :            #this option to exit the app
            exit()
        else:
            print("WRONG CHOICE !!!\n")
            continue
launchapp()