import math
m=int(input("enter"))
z=m
n=0
a=int(input("spacing"))
b=2*a-1
q=" "
while(n<=m-1):
    x=""
    r=0
    while(n>=r):
        c=int((math.factorial(n))/(math.factorial((n-r))*math.factorial(r)))
        s=str(c)
        t=s+(b*q)
        x=x+t
        r=r+1
    print(((z-1)*a*q)+x)
    n=n+1
    z=z-1
