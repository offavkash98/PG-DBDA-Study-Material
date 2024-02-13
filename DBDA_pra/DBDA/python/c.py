def addition(a,b):
    print(a+b)

def substration(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

x=int(input("enter a first value"))
y=int(input("enter a second value"))

print("---select---\n"\
      "1.addition\n"\
      "2.substration\n"\
      "3.multiply")

ch=int(input("enter your  choice"))

if ch==1:
    addition(x,y)

elif ch==2:
    substration(x,y)
elif ch==3:
    multiply(x,y)
    
else:
    print("wrong choice")
