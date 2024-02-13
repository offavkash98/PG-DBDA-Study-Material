'''
def discount(func):
    def wrapper(a,b,issunday=False):
        if issunday:
            tot=func(a,b)
            print(tot/2)
        else:
            tot=func(a,b)
            print(tot)
    return wrapper

@discount
def add(a,b,issunday=False):
    return a+b
add(10,20,False)
            
'''


def noZero(func):
    def inner(a,b):
        if b==0:
            print('deno can not be zero')
        else:
            func(a,b)
    return inner
@noZero
def div(a,b):
    print(a/b)

div(10,0)
            
