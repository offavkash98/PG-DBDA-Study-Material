#MULTILEVEL INH
class GrandParent:
    x = 10
    y = 20
    rn = 5
    def m1(self):
        print("m1---GrandParent")
    def m2(self):
        print("m2---GrandParent")

class Parent(GrandParent):
    x = 100
    d = 40
    def m1(self):
        print("m1---Parent")
    def m4(self):
        print("m4---Parent")

class Child(Parent):
    a = 30
    y = 200
    def m3(self):
        print("m3---Child")
    def m2(self):
        print("m2---Child")

ch = Child()
print(ch.rn)

print(Child.mro())
print('sdfgv',isinstance(ch,GrandParent))

print(issubclass(Child,Parent))
print(issubclass(Parent,Child))
print(issubclass(Child,object))
print(issubclass(Parent,object))


print(isinstance(ch,Child))
print(isinstance(ch,Parent))

