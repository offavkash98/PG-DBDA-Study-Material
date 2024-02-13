x=10
def m1():
    global x
    x=x+2
    print(x)
def m2():
    print(x)
def m3():
    global x
    x=x*4
    print(x)
m2()
m1()
m3()
m1()
m2()
