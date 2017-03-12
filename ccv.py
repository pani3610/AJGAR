import turtle as t
import math as m
j=4
while(j<=25):
    i=0
    while(i<=2*m.pi):
        v=0
        k=1
        for k in range(1,j,2):
            c=(1/k)*(m.sin(k*i))
            v=v+c
        t.setpos(25*i,50*v)
        i+=0.01
        
    j+=2
    t.clearscreen()
