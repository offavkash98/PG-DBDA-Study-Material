def gen():
    print('first yeils')
    yield 5
    print('second yeils')
    yield 10
    print('third yeils')
    yield 15

x = gen()
for i in x:
    print(i)
