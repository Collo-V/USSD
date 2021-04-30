import datetime
from cost_calculator import cost_calculator
from accounts import *


def sms():
    print("\n")
    sms_bal=balance_search("sms_bal:")
    while True:
        menu=["1.Create my sms Bundle","2. Daily sms","3.Weekly sms","4.Check balance","(Press any key to exit"]
        for item in menu:
            print(item)
        choice=input(":")
        if choice=="1":
            choice=input("(Press any letter to go back,0 to exit)\n How much do you want to spend?:")
            try:
                choice=float(choice)
                if choice<0:
                    print("value cannot be less than zero")
                    return
                spend=choice
                sms=spend*4
                break
            except:
                continue
        elif choice=="2":
            menu=["1.20sms @ 5bob","2. 200 sms @ 10bob","3. 500 sms @ 20bob","Press any letter to go back, 0 to exit"]
            for m in menu:
                print(m)
            choice=input(":")
            if choice=="1":
                sms=20
                spend=5
            elif choice=="2":
                sms=200
                spend=10
            elif choice=="3":
                sms=500
                spend=20
            elif choice=="0":return
            else:
                continue
            break
        elif choice=="3":
            menu=["1.400 sms @ 30","2. 700 sms @ 50bob","Press any letter to go back, 0 to exit"]
            for m in menu:
                print(m)
            choice=input(":")
            if choice=="1":
                sms=400
                spend=30
            elif choice=="2":
                sms=700
                spend=50
            elif choice=="0":return
            else:
                continue
            break
        elif choice=="4":
            date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
            time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
            print(f"{date} {time}:\n Your sms balace is {sms_bal}")
            return
            break
        else: return
    print(f"Please confirm purchase of {sms} sms for {spend}")
    choice=input("(Press 1 to confirm, any other character to deny:")
    if choice=="1":
        validity=cost_calculator(spend)
        if validity==1:
            sms_bal+=sms
            update_acc("sms_bal:",sms_bal)
            print(f"You have successfully purchased {sms} sms bundles")
        else:return
    else:
        print("Thank you for staying with us")
    return
