def projectmenu(userid):
    welcome_massage1 = "THIS IS PROJECTS MANAGMENT LIST"
    print(welcome_massage1.center(100,"="))
    print("Please , Choose one of the following options:")
    print("(1) Create Project. \n(2) View Current Projects. \n(3) Edit Project. \n(4) Delete Project. \n(5) Search For Project \n(6) Exit.")
    choice = input("==> ")

    if choice == "1":
        from Createproject import createproject
        createproject(userid)
    if choice == "2":
        from Viewproject import viewproject
        viewproject(userid)
    if choice == "3":
        from Editproject import editproject
        editproject(userid)
    if choice == "4":
        from Deleteproject import deleteproject
        deleteproject(userid)
    if choice == "5":
        from Searchforproject import searchproject
        searchproject(userid)
    if choice == "6":
        exit()

    else:
        print("WRONG CHOICE !!!\n")
        projectmenu(userid)