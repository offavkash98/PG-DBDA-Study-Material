'''
print("program starts")
try:
    import multipledispatch1
    d = int(input("enter sa number"))
    print(10/0)
    fh = open('njnjngj.txt')
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
except FileNotFoundError as fe:
    print(fe)
except ModuleNotFoundError as mnfe:
    print(mnfe,"\ninstall using 'pip insatll miltipledispatch'")

else:
    print('no exception')
finally:
    print("ALWAYS GOING TO EXCUTE")

print("program ends")    
'''

class AgeInvalidError(Exception):
    def __init__(self,msg):
        self.msg = msg

def termPolicyCalc(age):
    if age<0:
        raise AgeInvalidError ('age cannot be negative')
    installments = 30-age
    print(100000*installments)

a = int(input('enter your choice'))

try:
    termPolicyCalc(a)
except AgeInvalidError as aie:
    print(aie)

