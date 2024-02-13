#MULTIPLE INH
class Parent1:
    x = 10
    y = 20
    def m1(self):
        print("m1---Parent1")
    def m2(self):
        print("m2---Parent1")

class Parent2:
    x = 100
    d = 40
    def m1(self):
        print("m1---Parent2")
    def m4(self):
        print("m4---Parent2")

class Child(Parent1,Parent2):
    a = 30
    y = 200
    def m3(self):
        print("m3---Child")
    def m2(self):
        print("m2---Child")

c = Child()
print(c.x)#10
print(c.y)#200
print(c.a)#30
print(c.d)#40
c.m1()#m1---Parent1
c.m2()#m2---Child
c.m3()#m3---Child
c.m4()#m4---Parent2
print(Child.mro())
print(issubclass(Child,Parent1))
print(issubclass(Parent1,Child))
print(issubclass(Child,object))
print(issubclass(Parent1,object))


print(isinstance(c,Child))
print(isinstance(c,Parent1))

