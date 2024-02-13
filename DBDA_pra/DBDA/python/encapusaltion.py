class Car:
    __speed =100
    def showspeed(self):
        print(self.__speed)

    def update(self,s):
         self.__speed = s

c = Car()
c.showspeed()

c.update(150)
c.showspeed()
