'''
def sqr(n):
    return n*n
print(sqr(5))

'''

def inc(n):
    return n+1
print(inc(5))


from functools import reduce
marks= [10,20,30,40,50,60,70,80,90,95]


print(list(filter(lambda m:m<20,marks)))
print(list(filter(lambda m:m>=40,marks)))

print(list(map(lambda m:m+5,marks)))

print(reduce(lambda a,b:a+b,marks))
