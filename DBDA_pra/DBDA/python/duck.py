'''class Toyota:
    def max_speed(Self):
        print("max_speed toyota =200")

    def fuel_type(self):
        print("fuel_type toyota =diesel")


    def transmission(Self):
        print("transmisssion toyota = manual")


class kia:
    def max_speed(Self):
        print("max_speed kia =200")

    def fuel_type(self):
        print("fuel_type kia =diesel")


    def transmission(Self):
        print("transmisssion kia = automatic")

t=Toyota()
k=kia()



def car_details (obj):
    obj.max_speed()
    obj.fuel_type()
    obj.transmission()
for obj in (t,k):
    car_details(obj)'''
    


class book:
    def __init__(self,p):
        self.page = p

    def __str__(self):
        return f"totalpages={self.page}"
    def __add__(self,other):
        page = self.page+other.page
        b3 =book(page)
        return b3
b1 = book(200)
print(b1)

b2 = book(300)
print(b2)

print(b1+b2)

    
        
