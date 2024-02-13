'''class parent:
    parentx = 10
    def method_parent(self):
        print("method_parent of parent class")
class Child(parent):
    childy = 20
    def method_child(self):
        print("method_child of child class")

parentobj = parent()
childobj = Child()
print(parentobj.parentx)
print(childobj.childy)
print(childobj.parentx)
parentobj.method_parent()
childobj.method_child()
childobj.method_parent()
'''

class Parent:
    x = 10
    z = 30
    a = 5
    def method_a(self):
        print("method_a of parentclass")

class Child(Parent):
    x = 100
    y = 20
    a = 62
    def method_b(self):
        print("method_b of childclass")

ch = Child()
print(ch.x)
print(ch.y)
print(ch.z)
print(ch.a)
#print(ch.rn)

p = Parent()
print(p.z)
