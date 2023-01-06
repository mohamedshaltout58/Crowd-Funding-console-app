def viewproject1(userid):
    try:
        projectdata = open("projectinfo.txt", "r")
    except Exception as e:
        print(e)
    else:
        projects = projectdata.readlines()
        for project in projects:
            proj = project.strip("\n")
            projdata = proj.split(":")
            print(projdata)
        projectdata.close()
        return projects
def deleteproject(userid):
    allprojects = viewproject1(userid)
    print("Please Enter the Project You Want to Delete :")
    projecname = input("==> ")
    for project in allprojects:
        userproject = project.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == projecname and userid == userproject[0]:
            allprojects.remove(project)
            break
    else:
        print("The Project Is not exist please try again")
    w = open("projectinfo.txt", "w")
    w.writelines(allprojects)
    w.close()