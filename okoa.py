import datetime
from accounts import *

def okoa():
    print("\n")
    okoa_taken=balance_search("okoa_taken:")
    okoa_bal=balance_search("okoa_bal:")
    okoa_limit=balance_search("okoa_limit:")
    while True:
        menu=["1.Okoa","2.Check your okoa limit","3.Ckeck your Okoa debt","4.How okoa work","(Press any key to exit)"]
        for item in menu:
            print (item)
        choice=input(":")
        if choice=="4":
            print("Okoa allows you to get a creit of airtime within your limit.The limit is calculated based on your highest ever airtime balance. The loan is repayed automatically upon recharge")
            key= input("Press any key to go back or 00 to exit:")
            if key!="00":
                continue
            else: return
        elif choice=="2":
            print(f"Your Okoa limit is {okoa_limit}")
            key= input("Press any key to go back or 00 to exit:")
            if key!="00":
                continue
            else:return
        elif choice=="3":
            print(f"Your okoa debt is {okoa_taken}")
            key= input("Press any key to go back or 00 to exit:")
            if key!="00":
                continue
            else:return
        elif choice!="1":
            print("invalid choice. Try again")
            return
        else:
            break
    if okoa_limit==0:
        print("You are not qualified for okoa.Please recharge your line to use this service")
        return
    elif okoa_taken==okoa_limit:
        print("You have already reached your limit.Please pay your existing loan first")
        return
    else:
        while True:
            try:
                loan=float(input("(Press any  letter to exit ) How much do you want to okoa?:"))
                if loan<0:
                    print("value cannot be less than zero")
                    return
            except:
                return
            if loan<=0:
                print("The value can not be zero or less")
            if loan>okoa_limit-okoa_taken:
                print("Please try a lower amount")
                continue
            else:
                break
        okoa_taken+=loan
        interest=loan*10/100
        credit=loan-interest
        okoa_bal+=credit
        update_acc("okoa_taken:",okoa_taken)
        update_acc("okoa_bal:",okoa_bal)
        print(f"You have been credited with {credit} at an access fee of {interest}. Your okoa debt is {okoa_taken}")

