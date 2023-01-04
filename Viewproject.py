def viewproject(userid):
    print("Please Choose one of the following choices :")
    print("(1) Show Projects Title.\n(2) Show All Projects Data.")
    while True:
        choice = input("==> ")
        if choice == "1":
            try:
                projectdata = open("projectinfo.txt", "r")
            except Exception as e:
                print(e)
                continue
            else:
                projects = projectdata.readlines()
                for project in projects:
                    proj = project.strip("\n")
                    projdata = proj.split(":")
                    print(projdata[1])
                projectdata.close()
                break
        elif choice == "2":
            try:
                projectdata = open("projectinfo.txt", "r")
            except Exception as e:
                print(e)
                continue
            else:
                projects = projectdata.readlines()
                for project in projects:
                    proj = project.strip("\n")
                    projdata = proj.split(":")
                    print(projdata)
                projectdata.close()
                break
        else:
            print("Wrong Choice !!!")
            continue

