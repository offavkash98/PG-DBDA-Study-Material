#HIERARCHIAL INH
class Parent:
    x = 10
    y = 20
    def m1(self):
        print("m1---Parent")
    def m2(self):
        print("m2---Parent")

class Child1(Parent):
    x = 100
    d = 40
    def m1(self):
        print("m1---Child1")
    def m4(self):
        print("m4---Child1")

class Child2(Parent):
    a = 30
    y = 200
    def m3(self):
        print("m3---Child2")
    def m2(self):
        print("m2---Child2")

ch1 = Child1()
ch2 = Child2()
print(ch1.x)#100
print(ch1.y)#200
#print(ch1.a)#30
print(ch1.d)#40
ch1.m1()#ch1
ch1.m2()#p
#ch1.m3()#Error
ch1.m4()#ch1
print(Child2.mro())


print(issubclass(Child1,Parent))
print(issubclass(Parent,Child1))
print(issubclass(Child1,object))
print(issubclass(Parent,object))


print(isinstance(ch1,Child1))
print(isinstance(ch1,Parent))

