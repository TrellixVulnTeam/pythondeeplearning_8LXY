import re
psswd= input("please enter your password:")
v = True
while v:
    if (len(psswd)<6 or len(psswd)>16):
        break
    elif not re.search("[a-z]",psswd):
        break
    elif not re.search("[0-9]",psswd):
        break
    elif not re.search("[A-Z]",psswd):
        break
    elif not re.search("[[$@!*]",psswd):
        break
    elif re.search("\s",psswd):
        break
    else:
        print("Valid Password")
        v=False
        break

if v:
    print("Not a Valid Password")