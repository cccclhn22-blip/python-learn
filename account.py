def save_record(kind,amount,note):
    with open("money.txt","a") as f:
        f.write(kind +" "+ str(amount)+" "+ note + "\n")

def show_record():
    try:
        with open("money.txt","r") as f:
            balance=0
            for line in f:
                parts=line.strip().split()
                if parts[0]=="income":
                    balance=balance+float(parts[1])
                else:
                    balance=balance-float(parts[1])
                print(line.strip())   
            print("balance:",balance) 
    except FileNotFoundError:
        print("empty, make an new one")

while True:
    print("1-add 2-check 3-exit")
    choice = input("choose: ")
    if choice=="1":
        kind=input("income or spence")
        amount=float(input("amount: "))
        note=input("note:")
        save_record(kind,amount,note)
        print("done")
    elif choice=="2":
        show_record()
    elif choice=="3":
        break    