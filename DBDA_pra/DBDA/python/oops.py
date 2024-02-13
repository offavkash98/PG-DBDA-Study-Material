class A:
    def m1(self):
        print("m1----A")

class B:
    def m2(self):
        print("m2----B")
        A.m1(self)

b=B()
b.m2()
        
