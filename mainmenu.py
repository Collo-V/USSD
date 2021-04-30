import datetime
from okoa import okoa
from sms import sms
from bundles import bundles
from bonga import bonga
from balances import balances_check
from accounts import *



def mainmenu():
    print("\n")
    menu=["Please select a service","1.Top up","2.Bundles","3.Sms bundles","4.bonga","5. Okoa","6.Check balances","Press any key to exit"]
    for item in menu:
        print (item)
    choice=input(":")
    if choice=="1":print("Please dial *141*SractchcardPin#")
    elif choice=="2":bundles()
    elif choice=="3":sms()
    elif choice=="4":bonga()
    elif choice=="5":okoa()
    elif choice=="6":balances_check()
    else:return

