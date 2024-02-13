bal = 5000
def deposite(amt):
    global bal
    bal=bal+amt
def withdrawl(amt):
    global bal
    bal=bal-amt
def bal_check():
    print(bal)

deposite(1000)
bal_check()
deposite(2000)
bal_check()
withdrawl(1000)
bal_check()
deposite(2000) #9000
bal_check()
withdrawl(3000)#6000
bal_check()


x=int(input("how much amount want to deposite "))
deposite(x)
bal_check()
