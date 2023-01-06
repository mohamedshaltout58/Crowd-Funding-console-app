import time
def validatedate(date):
    try:
        validate = time.strptime(date, '%d/%m/%Y')
        if validate:
            return True
    except Exception as e:
        print(e)
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
def editproject(userid):
    allprojects=viewproject1(userid)
    print("Please Enter the Project You Want to Edit :")
    projectname =  input("==> ")
    for i in allprojects:
        userproject = i.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == projectname and userid==userproject[0]:
            print(allprojects)
            print("Please Enter Your Edit Choice :\n(1) Edit Project Title\n(2) Edit Project Details\n(3) Edit Project Target\n(4) Edit Project Start Date\n(5) Edit Project End Date")
            key_name = input("==> ")
            if key_name == "1":
                print("Please , Enter The New Title :")
                ntitle = input("==> ")
                userproject[1]= ntitle
            elif key_name == "2":
                print("Please , Enter The New Detail :")
                ndetail = input("==> ")
                userproject[2]= ndetail
            elif key_name == "3":
                while True:
                    print("Please , Enter The New Target :")
                    ntarget = input("==> ")
                    try:
                        val = int(ntarget)
                        if val < 0:
                            print("Wrong Entry!!!")
                            continue
                        break
                    except ValueError:
                        print("Please Enter Right New Target Value")
                userproject[3] = ntarget
            elif key_name == "4":
                while True:
                    print("Please ,Enter The New Project START TIME (dd/mm/yyyy): ")
                    nstarttime = input("==> ")
                    if validatedate(nstarttime) and (nstarttime < userproject[5]):
                        userproject[4] = nstarttime
                        break
                    else:
                        print("Wrong Date Value!!!")
                        continue
            elif key_name == "5":
                while True:
                    print("Please ,Enter The New Project END TIME (dd/mm/yyyy): ")
                    nendtime = input("==> ")
                    if validatedate(nendtime) and (nendtime > userproject[4]):
                        userproject[5] = nendtime
                        break
                    else:
                        print("Wrong Date Value!!!")
                        continue
            else:
                print("WRONG INPUT !!!")
                editproject(userid)

            updated_project = ":".join(userproject)
            updated_project = f"{updated_project}\n"
            project_index = allprojects.index(i)
            print(project_index)
            allprojects[project_index] = updated_project
            break
    final = open("projectinfo.txt", "w")
    final.writelines(allprojects)
    final.close()
