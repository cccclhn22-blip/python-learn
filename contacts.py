contacts={}
while True:
    print("1-add","2-check","3-del","4-exit")
    choice=input("select one: ")
    if choice=="1":
        name=input("name:")
        phone=input("phone number:")
        contacts[name]=phone
        print("added")
    elif choice=="2":
        name=input("which person you want to check?: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("not exist")
    elif choice=="3":
        name=input("which person you want to delete?:")
        if name in contacts:
            del(contacts[name])
            print("delete succe")
        else:
            print("not exitst")
    elif choice=="4":
        break
    else:
        print("no this option")