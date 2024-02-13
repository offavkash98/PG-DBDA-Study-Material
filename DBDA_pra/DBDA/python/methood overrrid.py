'''class Calc:
    def div(self,a,b):
        print(a/b)

class AdvCalc(Calc):
    def div(self,a,b):
        if b==0:
            print("donot canot be zero")
        else:
            print(a/b)
ac=AdvCalc()
ac.div(10,0)
'''


from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    print("add with 2 int args calles")
    print(a+b)

@dispatch(int,int,int)    
def add(a,b,c):
    print("add with 3 int args calles")
    print(a+b+c)
    
@dispatch(str,str)    
def add(fn,ln):
    print("add with 3 int args calles")
    print(fn+ln)

    
print(10,20)
print(10,20,30)
add("cjc","pune")
