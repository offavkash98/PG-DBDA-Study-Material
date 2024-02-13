def addition(a,b):
    c=a+b
    return c
def substration(a,b):
    return a-b
def multiply(a,b):
    return a*b
print("---select---\n"\
      "1.addition\n"\
      "2.substration\n"\
      "3.multiply\n"\
      "4.exit")
while True:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    ch=int(input("enter your choice"))

    if ch==1:
        s=addition(x,y)
        print(s)

    elif ch==2:
         x=substration(x,y)
         print(x)
     
    elif ch==3:
        x=multiply(x,y)
        print(x)
    
    elif ch==4:
        break
    else:
        print("your choice")
    
