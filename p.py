import random as r
m=0
n=0
def f1():
    a=r.randrange(100)
    b=r.randrange(20)
    z=a*b
    c=str(a)+" x "+str(b)
    d=int(raw_input(c))
    if(d==z):
        print 'right'
        global m
        m+=1
    else:
        print 'wrong'
        global n
        n+=1
    
def f2():
    a=r.randrange(1000)
    b=r.randrange(1000)
    e=r.randrange(1000)
    z=a+b+e
    c=str(a)+"+"+str(b)+"+"+str(e)
    d=int(raw_input(c))
    if(d==z):
        print 'right'
        global m
        m+=1
    else:
        print 'wrong'
        global n
        n+=1

m=0
n=0
d={1:f1(),2:f2()}
while(1>0):
    global m
    
    global n
    m,n=0,0
    i=0
    while(i<10):
        d[r.randrange(1,3)]
    print 'correct'+str(m)
    print 'incorrect'+str(n)
    v=raw_input('go')
    if(v==''):
        break

    
    
