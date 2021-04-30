from accounts import *

def cost_calculator(spend):
    okoa_bal=balance_search("okoa_bal:")
    airtime_bal=balance_search("airtime_bal:")
    bal=okoa_bal+airtime_bal
    if spend>bal:
        print("You do not have sufficient airtime to make this transaction.Please recharge or Okoa")
        return 0
    else:
        if okoa_bal>=spend:
            okoa_bal-=spend
        else:
            spend-=okoa_bal
            airtime_bal-=spend
            okoa_bal=0

        update_acc("okoa_bal:",okoa_bal)
        update_acc("airtime_bal:",airtime_bal)
        return 1

