import datetime
from accounts import *


bob10=["12345","12354","12435","12453","12534","12543","13245","13254"]
bob20=["13425","13452",'13524',"13542","14235","14253","14235","14352"]
bob50=["14523","14532","15234","15243","15324","15342","15423","15432"]

def scratch_values(code):    
    if code in bob10:
        value = 10
        bongapoints=2
    elif code in bob20:
        value=20
        bongapoints=4
    elif code in bob50:
        value=50
        bongapoints=10
    else:
        value=0
        bongapoints=0
    return value,bongapoints





def recharge(ussd_code):
    okoa_taken=balance_search("okoa_taken:")
    airtime_bal=balance_search("airtime_bal:")
    okoa_limit=balance_search("okoa_limit:")
    bonga_bal=balance_search("bonga_bal:")
    if ussd_code[-1]!="#":
        print("Wrong format. every USSD must end with a '#' ")
        return
    code=ussd_code[5:10]
    value=scratch_values(code)[0]
    bongapoints=scratch_values(code)[1]
    if value==0:
       print("The voucher you have entered does not exist")
    else:
        print(f"You have successfully recharged with {value}")
        if okoa_taken>0:
            if okoa_taken<=value:
                print(f"{okoa_taken} has been deducted to repay your okoa debt.The debt is now fully settled")
                okoa_taken=0
                value-=okoa_taken
            else:
                print(f"{value} has been deducted to to repay your okoa ebt. Dial *131# to check your remaining debt")
                okoa_taken-=value
                value=0
        airtime_bal+=value
        bonga_bal+=bongapoints
        if airtime_bal*1.5>okoa_limit:
            okoa_limit=int(airtime_bal*1.5)
        update_acc("okoa_taken:",okoa_taken)
        update_acc("airtime_bal:",airtime_bal)
        update_acc("okoa_limit:",okoa_limit)
        update_acc("bonga_bal:",bonga_bal)
        print(f"Your new balance is {airtime_bal}")


