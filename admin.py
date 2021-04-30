from accounts import*

open_acc()
menukeys={
    "okoa bal":"okoa_bal:",
    "okoa taken":"okoa_taken:",
    "airtime balance":"airtime_bal:",
    "bonga balance":"bonga_bal:",
    "bundle balance":"bundle_bal:",
    "sms balance":"sms_bal:"
}
while True:
    menu=["okoa bal","okoa taken","airtime balance","bonga balance","bundle balance","sms balance"]
    print("What do you want to change?")
    for n in range(len(menu)):
        print(f"{n}.{menu[n]}")
    choice=int(input(":")) 
    while True:
        
        try:
            value=int(input(f"update {menu[choice]} to what:(press any keyto go back)"))
            if value<0:
                print("value can never be negative")
                continue
            else:break
        except:
            break
    break
update_acc(menukeys.get(menu[choice]),value)\
print(f"{menu[choice]} updated successfully!")

