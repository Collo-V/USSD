import datetime
from accounts import *
from recharge import scratch_values,recharge
from okoa import okoa
from sms import sms
from bundles import bundles
from bonga import bonga
from mainmenu import mainmenu
from balances import balances_check





def airtime_check():
    open_acc()
    airtime_bal=balance_search("airtime_bal:")
    date = datetime.datetime.now().strftime("%d"" ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    if airtime_bal==0:
        print(f"Dear customer, your balance is 0")
    else:
        print(f"Your balace on {date} at {time} was {airtime_bal}")



 


ussdkeys={
    "*100#":mainmenu,
    "*126#":bonga,
    "*131#":okoa,
    "*144#":airtime_check,
    "*544#":bundles,
    "*188#":sms,
    "*144*4#":balances_check
}

while True:
    
    ussd_code=input("Enter USSD Code:")
    if ussd_code[0:5]=="*141*":
        recharge(ussd_code)        
    elif ussd_code in ussdkeys:
        functioncall=ussdkeys.get(ussd_code)
        function=functioncall()
        print("\n")
    else:
        print("Invalid USSD.Please try again")
        continue


