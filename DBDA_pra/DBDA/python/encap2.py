class Student:
    __rn = 0
    __name =''

    def setRn(self,r):
        self.__rn = r

    def getRn(Self):
        return Self.__rn

    def setName(self,n):
        self.__name = n

    def getName(self):
        return self.__name



s1 = Student()
print(s1.getRn())
print(s1.getName())
s1.setRn(1)
s1.setName('abcd')
print(s1.getRn())
print(s1.getName())
