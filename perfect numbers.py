a=int(input("enter"))
k=2
t=1
while(t<=a):
    print(k)
    m=(2**k)-1
    n=2
    while(n<m):
        c=m%n
        n=n+1
        if (c==0):
            break
    else:
        z=m
        f=m*(2**(k-1))
        
        print(f)
        t=t+1
    k=k+1
        
    
