'''fs1 = frozenset({1,2,3,4,5,"cjc"})
fs2 = frozenset({6,6,7,8,9,10})

s = {fs1,fs2}
print(s)
print(fs1,fs2)
print(fs1&fs2)
print(fs1-fs2)

for i in fs1:
    print(i,type(i))
for i in s:
    for j in i:
        print(j)
'''


