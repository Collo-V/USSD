import datetime
from cost_calculator import cost_calculator
from accounts import *

def bundles():
    print("\n")
    bundle_bal=balance_search("bundle_bal:")
    
    while True:
        menu=["0.Buy 2Gb @250 and get 1 gb free","1.Create my Bundle","2. Daily bundles","3.Weekly bundles","4.Check balance","(Press any key to exit"]
        for item in menu:
            print(item)
        choice=input(":")
        if choice=="0":
            Mbs=3072
            spend=250
            break
        if choice=="1":
            choice=input("(Press any letter to go back,0 to exit)\n How much do you want to spend?:")
            try:
                choice=float(choice)
                if choice<0:
                    print("value cannot be less than zero")
                    return
                if choice==0:
                    return
                spend=choice
                Mbs=spend*5
                break
            except:
                continue
        elif choice=="2":
            menu=["1.Sh 20: 100mbs","2. sh50: 300Mbs","3. sh 100: 1.5Gb","Press any letter to go back, 0 to exit"]
            for m in menu:
                print(m)
            choice=input(":")
            if choice=="1":
                Mbs=100
                spend=20
            elif choice=="2":
                Mbs=300
                spend=50
            elif choice=="3":
                Mbs=1536
                spend=100
            elif choice=="0":return
            else:
                continue
            break
        elif choice=="3":
            menu=["1.500 Mbs @ 100Bob","2. 2Gb @ 200bob","3.4Gb @ 300Bob","4. 8Gb @ 500Bob","Press any letter to go back, 0 to exit"]
            for m in menu:
                print(m)
            choice=input(":")
            if choice=="1":
                Mbs=500
                spend=100
            elif choice=="2":
                Mbs=2048
                spend=200
            elif choice=="3":
                Mbs=4096
                spend=300
            elif choice=="4":
                Mbs=8192
                spend=500
            elif choice=="0":return
            else:
                continue
            break
        elif choice=="4":
            date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
            time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
            print(f"{date} {time}:\n Your bundles balace is {accounts.bundle_bal}")
            return
            break
        else: return
    print(f"Please confirm purchase of {Mbs} Mbs for {spend}")
    choice=input("(Press 1 to confirm, any other character to deny:")
    if choice=="1":
        validity=cost_calculator(spend)
        if validity==1:
            bundle_bal+=Mbs
            update_acc("bundle_bal:",bundle_bal)
            print(f"You have successfully purchased {Mbs} Mbs")
        else:return
    else:
        print("Thank you for staying with us")
    return

        
