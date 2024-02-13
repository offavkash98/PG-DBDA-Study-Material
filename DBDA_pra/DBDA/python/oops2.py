class person:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g

    def __str__(self):
        return f'{self.name},{self.age}{self.gender}'
    
class Student(person):
    def __init__(self,n,a,g,r,m):
        super().__init__(n,a,g)
        self.rn = r
        self.marks = m

    def __str__(self):
        print(super().__str__())
        return f'{self.name},{self.marks}'

s1 = Student('abc',20,'f',1,10)
print(s1)
