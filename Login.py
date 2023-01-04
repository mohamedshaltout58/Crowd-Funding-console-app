from ProjectMenu import projectmenu
def login():
    mail = input("Please , Enter Your Email : ")
    password = input("Please , Enter Your Password : ")
    try:
        fileobject = open('userinfo.txt','r')
    except Exception as e:
        print(e)
    else:
        users = fileobject.readlines()
        for u in users:
            userdata = u.strip("\n")
            userinfo = userdata.split(":")

            if userinfo[3] == mail and userinfo[4] == password:
                print("-----------Logged in---------------")
                projectmenu(userinfo[0])
                break
        else:
            print("USER NOT FOUND")
            login()

    fileobject.close()
