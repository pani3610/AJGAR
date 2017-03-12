import math
x=int(input("Enter x"))
b=int(input("Enter n"))
m=str(x)
z=0
n=3
s=""
while(z<b-1):
    t=str(n)
    if (z%2==0):
        k="+"
    else:
        k="-"
    c=k+"("+m+"^"+t+"/"+t+"!)"
    s=s+c
    z=z+1
    n=n+2
print(m+s)
    
                        
