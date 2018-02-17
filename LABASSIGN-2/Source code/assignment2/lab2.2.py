v = int(input("enter number of phonedetails : "))
phonedetails = []
phone_dict = {}
for i in range(v) :
    phone_dict["name"] = input("Enter name ")
    phone_dict["number"] = input("Enter number ")
    phone_dict["email"] = input("Enter email ")
    phonedetails.append(phone_dict.copy())
print(phonedetails)
optn = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
if optn=='a':
    name = str(input("Enter the name: "))
    for a in phonedetails:
        if a['name'] == name:
            print(a)
    optn = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
if optn=='b':
    number = str(input("Enter the number: "))
    for a in phonedetails:
        if a['number'] == number:
            print(a)
    optn = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
if optn=='c':
    name = str(input("Enter the name: "))
    number = int(input("Enter the number: "))
    for index,a in enumerate(phonedetails):
        if a['name'] == name:
            phonedetails[index]['number']=number
    print(phonedetails)
    optn = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:\n "))
if optn=='d' :
    exit()