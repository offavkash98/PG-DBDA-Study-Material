class Student:
    rn=0
    name=''
    marks=0.0

    def setData(self,r,n,m):
        self.rn = r
        self.name = n
        self.marks = m

    def getData(self):
        print(self.rn)
        print(self.name)
        print(self.marks)

s1 = Student()
s1.getData()
s1.setData(1,"abc",10)
s1.getData()

s2 = Student()
s2.getData()
s2.setData(2,"defg",10)
s2.getData()


