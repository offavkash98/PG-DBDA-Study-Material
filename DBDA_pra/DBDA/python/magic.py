
class Student:
    def __init__(self):
        print("contructior got called")
    def m1(self):
         print("m1 get called")
    def __str__(self):
        print("str got called")
        return "cjc"
s1 = Student()
print(s1)

'''
class Student:
    def __init__(self,r,n):
        self.rn = r
        self.name = n
    def __str__(self):
        return f"Rn={self.rn},name={self.name}"
s1=Student(1,"abc")
print(s1)
'''
