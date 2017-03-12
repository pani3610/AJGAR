#First,Go to Options>>Configure IDLE...>>change Font size to 7.
import math
a="■"
k=" "
d=" "

x=1
r="."
m=1
while (1>0):
    while(x<=180):
        t=x*(math.pi/180)
        c=int((math.sin(t))//0.02)
        n=50-c
        print((n*d)+(a*c)+(a*c)+(n*d))
        x=x+2
        if (m%2==0):
            print((n*d)+(k*c)+(k*c)+(n*d))
        m=m+1
    x=1
    m=1    
    
    
