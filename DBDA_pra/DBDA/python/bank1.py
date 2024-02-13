bal=5000
def deposite(amt,bal):
    bal=bal+amt
    return bal
def withdrawl(amt,bal):
    if bal>amt:
        print("insufficient funds")
    else:
        bal=amt-bal
        return bal
def bal_check(bal):
    print(bal)
    
x=int(input("how much balance you want to deposite"))
y=int(input("how much balance you want to withdrawal"))

bal=deposite(x,bal)
bal_check(bal)
bal=deposite(2000,bal)
bal_check(bal)
bal=withdrawl(2000,bal)
bal_check(bal)
