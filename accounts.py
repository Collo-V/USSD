balnames=[]
bals=[]

def open_acc():
    global balnames,bals
    balnames=[]
    bals=[]
    with open("USSD/accounts.txt","r") as balances:
        balances.seek(0)
        balances=balances.read().split()
        acc=[]
        for n in balances:
            acc=[m for m in n if m.isdigit()]
            y=''
            
            for x in range(len(acc)):
               y+=acc[x]

            y=int(y)
            bals.append(y)
        for n in balances:
            acc=''.join([m for m in n if not m.isdigit()]) 
            balnames.append(acc)
    return

def balance_search(balname):
    open_acc()
    indx=balnames.index(balname)
    value=bals[indx]
    
    return value


def update_acc(balname,value):
    open_acc()
    indx=balnames.index(balname)
    bals[indx]=int(value)
    with open("USSD/accounts.txt","w") as balances:
        for n in range(len(bals)):
            balances.writelines(f"{balnames[n]}{bals[n]}\n")
    


