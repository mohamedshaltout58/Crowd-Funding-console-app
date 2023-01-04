#give new user new id number according to the number of lines at userinfo.txt
def userid():
    with open(r"userinfo.txt", 'r') as readrows:
        x = len(readrows.readlines())
        return x+1
userid()