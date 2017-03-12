import math
a=1
n=1
d=1
while(n<100000000):
    x=0
    while(a>0):
        c=a%10
        a=a//10
        t=c**d
        x=x+t
    if(x==n):
        print(n)
    n=n+1
    a=n
    d=int(math.log(n,10))+1
          
