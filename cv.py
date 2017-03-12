import math
x=int(input("Enter x"))
b=int(input("Enter n"))
m="x"
f=0
z=0
n=3
s=""
print(x)
while(z<b-1):
    l=((-1)**z)*(x**n)/(math.factorial(n))
    t=str(n)
    if (z%2==0):
        k="+"
    else:
        k="-"
    c=k+"("+m+"^"+t+"/"+t+"!)"
    s=s+c
    f=f+l
    z=z+1
    n=n+2
print(m+s,"=",x+f)
    
                        
