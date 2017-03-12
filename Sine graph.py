#First,Go to Options>>Configure IDLE...>>change Font size to 7.
import math
a="■"
d="$"
k=100
x=1
f=00000
m=0
while (1>0):
    while(x<=180):
        t=x*(math.pi/180)
        c=int((math.sin(t))//0.01)
        n=99-c
        print((k*d)+(a*c)+(n*d))
        x=x+2
        m=0
        while(m<f):
            m=m+1
    x=1
    while(x<=180):
        t=x*(math.pi/180)
        c=int((math.sin(t))//0.01)
        n=99-c
        print((n*d)+(a*c)+(k*d))
        x=x+2
        m=0
        while(m<f):
            m=m+1
    x=1
    
