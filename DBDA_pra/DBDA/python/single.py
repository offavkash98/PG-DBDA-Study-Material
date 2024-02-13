
#SINGLE INH
class Parent:
    x = 10
    y = 20
    def m1(self):
        print("m1---Parent")
    def m2(self):
        print("m2---Parent")

class Child(Parent):
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
c.m1()#m1---Parent
c.m2()#m2---Child
c.m3()#m3---Child

print(issubclass(Child,Parent))
print(issubclass(Parent,Child))
print(issubclass(Child,object))
print(issubclass(Parent,object))


print(isinstance(c,Child))
print(isinstance(c,Parent))

