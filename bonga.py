
import datetime
import importlib
#import accounts
from accounts import*
from balances import *


def bonga():
    print("\n")
    bundle_bal=balance_search("bundle_bal:")
    sms_bal=balance_search("sms_bal:")
    airtime_bal=balance_search("airtime_bal:")
    bonga_bal=balance_search("bonga_bal:")
    while True:
        menu=["0.Get 8Ksh for 25 points","1.Check bonga points","2.Redeem bonga points","(Press any key to exit)"]
        for item in menu:
            print(item)
        choice=input(":")
        if choice=="0":
            redeem_points=25
            rdm=8
            rtype="airtime"
            
        elif choice=="1":
            date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
            time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
            print(f"{date} {time}:\n Your bonga balance is {bonga_bal} points")
            choice=input("Press any key to go back,00 to exit:")
            if choice!="00":
                continue
            else: return
        
        
        elif choice=="2":
            while True:
                menu=["1.Free airtime","2.Free Internet","3.Free sms","(Press any key to exit)"]
                for item in menu:
                    print(item)
                choice=input(":")
                if choice=="1":
                    rtype="airtime"
                elif choice=="2":
                    rtype="Mbs"
                elif choice=="3":
                    rtype="sms"
                else: return
                while True:
                    choice=input("(Press any letter to go back,0 to exit)\n How many points do you want to redeem?(minimum is 10):")
                    try:
                        choice=float(choice)
                        if choice<10:
                            print("Minimum is 10")
                            continue
                        else:
                            break
                    except:
                        break
                if type(choice)!=float:
                    continue 
                else:
                    break
            if choice>=10:
                redeem_points=choice
            else: return
        else: return
        if redeem_points>bonga_bal:
            print("You do not have enough points")
            return
        else:
            if rtype=="airtime":
                rdm=redeem_points/3
            elif rtype=="Mbs":
                rdm=redeem_points
            else:
                rdm=redeem_points/4
            print(f"Please confirm redemption of {redeem_points} points for {rdm:.0f} {rtype}")
            choice=input("Press 1 to confirm, any other key to deny")
            if choice!="1":
                return
            else:
                if rtype=="airtime":
                    airtime_bal+=rdm
                    sms_bal=0
                    bundle_bal=0
                elif rtype=="Mbs":
                    bundle_bal+=rdm
                    sms_bal=0
                    airtime_bal=0
                else:
                    sms_bal+=rdm
                    airtime_bal=0
                    bundle_bal=0
        bonga_bal-=redeem_points

        update_acc("bundle_bal:",bundle_bal)
        update_acc("sms_bal:",sms_bal)
        update_acc("airtime_bal:",airtime_bal)
        update_acc("bonga_bal:",bonga_bal)

        print(f"You have redeemed {redeem_points} points worth of {rdm:.0f} {rtype}")
        return
