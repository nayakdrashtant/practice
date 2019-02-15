import os
def listoffiles():
    path = os.getcwd()
    dir = os.listdir(path)
    for d in dir:
        print(d)


listoffiles()
