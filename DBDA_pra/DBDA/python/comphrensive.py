li = [1,2,3,4,5,6,7,8,9,10]

sqrs = [i*i for i in li]
print(sqrs)

evens = {i*i for i in li if i%2==0}
print(evens)

newli = ['even' if i%2==0 else 'odd' for i in li]
print(newli)

newmarks = [i+5 for i in li ]
print(newmarks)
newmarksDi = {i:1+5 for i in li}
print(newmarksDi)
