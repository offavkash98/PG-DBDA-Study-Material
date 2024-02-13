'''
class MyRange:
    def __init__(self,s,e):
        self.st = s
        self.en = e
    def __iter__(self):
        return self
    def __next__(self):
        if self.st<self.en:
            self.st = self.st+1
            return self.st
        else:
            raise StopIteration
        
mr_iterable = MyRange(10,20)

for i in mr_iterable:
    print(i)
        


'''
class CustomIterator:
    def __init__(self,s,e,i):
        self.st=s
        self.en=e
        self.inc=i
        
    def __iter__(self):
        return (self)

    def __next__(self):
        if self.st<self.en:
            self.st = self.st+1
            return self.st
        else:
            raise StopIteration
        
custom_iterable = CustomIterator(0,50,5)

for i in custom_iterable:
    print(i)
        
 
    
