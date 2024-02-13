d2 = {}
print(d2)
d2[1]=1
print(d2)
d2[2]=4
print(d2)
d2['cjc']=9
print(d2)
d2.update({4:1,5:25,6:30})
print(d2)
d2.pop('cjc')
print(d2)
d2.popitem()
print(d2)

print(d2[2])
print(d2[4])
print(d2.get(2))
print(d2.get(4))
print(d2.get(3))
