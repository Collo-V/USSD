import datetime
import importlib
from accounts import *


def balances_check():
    print("\n")
    bundle_bal=balance_search("bundle_bal:")
    sms_bal=balance_search("sms_bal:")
    airtime_bal=balance_search("airtime_bal:")
    bonga_bal=balance_search("bonga_bal:")
    okoa_bal=balance_search("okoa_bal:")

    date = datetime.datetime.now().strftime("%d""th ""%B"" " "%Y")
    time= datetime.datetime.now().strftime("%I"":""%M"" " "%p")
    print(f"{date} {time}:\n Airtime:{airtime_bal} Bob\n {bundle_bal} Mbs Internet bundles\n {sms_bal} On net sms\n {bonga_bal} Bongapoints\n {okoa_bal} Bob Okoa balance")


