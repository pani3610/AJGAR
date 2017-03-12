a=int()
b=int()
c=b-a
def zak(a,b,m=b):
    k=0
    while(a<=b and k<m):
        n=2
        while(n<a):
            t=a%n
            n=n+1
            if(t==0):
                break
        else:
            print(a)
            k=k+1
        a=a+1
