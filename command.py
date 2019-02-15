



import os
def command(cmd):
    cmd = str(cmd)
    fr = os.popen(cmd)
    res = fr.read()
    print(res)

var = input("Enter linux command to perform operation:")
command(var)
