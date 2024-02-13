def gen():

    i=0
    while i<100:
        yield i
        i=i+2

g=gen()
for i in g:
    print(i)
