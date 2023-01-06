import time

def createproject(userid):
    while True:
        print("Please , Add your project TITLE : ")
        title = input("==> ")
        if len(title) > 20 :
            print("Your Title Is Too Long !!!")
            continue
        else:
            break
    print("Please , Add your project DETAILS : ")
    details = input("==> ")
    while True:
        print("Please , Add your project TOTAL TARGET : ")
        TotalTarget = input("==> ")
        try:
            val = int(TotalTarget)
            if val < 0:
                print("Wrong Entry!!!")
                continue
            break
        except ValueError :
            print("Please Enter Right Target Value")

    def validatedate(date):
        try:
            validate = time.strptime(date, '%d/%m/%Y')
            if validate:
                return True
        except Exception as e:
            print(e)
    while True:
        print("Please , Add your project START TIME (dd/mm/yyyy): ")
        StartTime = input("==> ")
        if validatedate(StartTime):
            break
        else:
            print("Wrong Date Value!!!")
            continue
    while True:
        print("Please , Add your project END TIME (dd/mm/yyyy): ")
        EndTime = input("==> ")
        if validatedate(EndTime) and (EndTime > StartTime):
            project_data = open("projectinfo.txt", "a")
            projdata = f"{userid}:{title}:{details}:{TotalTarget}:{StartTime}:{EndTime}\n"
            project_data.write(projdata)
            project_data.close()
            print(f"Congratulations , Your Project {title} Was Created Successfuly".center(100,"="))
            break
        else:
            print("Wrong Date Value!!!")
            continue
