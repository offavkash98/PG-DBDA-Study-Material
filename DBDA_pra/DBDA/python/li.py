'''li =[10,20,30,40,50,60,70,80,90,100]

for i in li:
    print(i,type(i))
    
print(max(li))
print(min(li))
print(sum(li))
print(len(li))
print(li.count(10))
print(li.index(100))
'''
marks=[]
print(marks)

for i in range(5):
    m=float(input("enter your marks"))
    marks.append(m)
print(marks)
print(max(marks))    
print(min(marks))
print(sum(marks))
print(len(marks))
print(marks.count(10))
print(marks.index(45))
