n=int(input("enter n of nCr : "))
r=int(input("enter r of nCr : "))

b=r
h=1
a=n
f=1
while (n>a-r):
    f=f*n
    n=n-1
while (r>1):
    h=h*r
    r=r-1
k=f/h
    
print(a,"C",b,"is",int(k))

