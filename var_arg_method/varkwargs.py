def person_name(**kwargs):
    print(kwargs)

person_name(first="Sachin",middle="ramesh",last="tendulkar")



#Thejaswi has 6month exp in sap
def emp_details(**kwargs):
    # print(kwargs)
    name=kwargs.get("name")
    exp=kwargs.get("exp")
    dom=kwargs.get("domain")
    print(f"{name} has {exp} experience in {dom}")
emp_details(name="Thejaswi",exp="6 month",domain="SAP")    


#your sbi 1234 ac balance is INR 25000
def bank_balance(**kwargs):
    # print(kwargs)
    bank=kwargs.get("bank")
    ac=kwargs.get("ac_no")
    bal=kwargs.get("balance")
    print(f"your {bank} {ac} ac balance is INR {bal}")    
bank_balance(bank="SBI",ac_no=1234,balance="25000")    