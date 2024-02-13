class A:
    def m1(self):
        print("m1----a")

class B(A):
    def m1(self):
        print("-----")
        super().m1()

b = B()
b.m1
