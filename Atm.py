#accounts
username=["vasu","bala","raja","kumar","vignesh"]
#username&pin
vasu=1234
bala=5678
raja=9012
kumar=3456
vignesh=7890
#accountbalance
vasu_b=50000
bala_b=100000
raja_b=150000
kumar_b=200000
vignesh_b=250000

def vasu_withdraw():
    amount=int(input("Enter withdraw amount:"))
    balance=vasu_b-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>vasu_b:
        print("Not Valid")
def vasu_be():
    print(f"Your Balance Amount Is:{vasu_b}")

def bala_withdraw():
    print("")
    amount=int(input("Enter withdraw amount:"))
    balance=bala_b-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>vasu_b:
        print("Not Valid")
def bala_be():
    print(f"Your Balance Amount Is:{bala_b}")

def raja_withdraw():
    print("")
    amount=int(input("Enter withdraw amount:"))
    balance=raja_b-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>vasu_b:
        print("Not Valid")
def raja_be():
    print(f"Your Balance Amount Is:{raja_b}")

def kumar_withdraw():
    print("")
    amount=int(input("Enter withdraw amount:"))
    balance=kumar_b-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>vasu_b:
        print("Not Valid")
def kumar_be():
    print(f"Your Balance Amount Is:{kumar_b}")

def vignesh_withdraw():
    print("")
    amount=int(input("Enter withdraw amount:"))
    balance=vignesh_b-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>vasu_b:
        print("Not Valid")

def vignesh_be():
    print(f"Your Balance Amount Is:{vignesh_b}")

print("***Welcome To Atm***")
user=input("Enter Your Name:").lower().strip()
if user in username:
    pin=int(input("Enter Your Pin:"))
    print("")
    if user=="vasu" and pin==1234:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            vasu_withdraw()
        elif choose==2:
            vasu_be()
    elif user=="bala" and pin==5678:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            bala_withdraw()
        elif choose==2:
            bala_be()
    elif user=="raja" and pin==9012:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            raja_withdraw()
        elif choose==2:
            raja_be()
    elif user=="kumar" and pin==3456:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            kumar_withdraw()
        elif choose==2:
            kumar_be()
    elif user=="vignesh" and pin==7890:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            vignesh_withdraw()
        elif choose==2:
            vignesh_be()






