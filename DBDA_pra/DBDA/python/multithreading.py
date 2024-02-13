from threading import currentThread,Thread

def evens(end,steps):
    for i in range(0,end,steps):
        print(i,currentThread().name)

def odds():
    for i in range(1,52,2):
        print(i,currentThread().name)

t1=Thread(target=evens,name='evenThread',args=(51,5))
t2=Thread(target=odds)
t2.setName(name='oddTHread')
t1.start()
t2.start()


        
