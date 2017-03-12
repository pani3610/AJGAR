while(1>0):
    a=int(input("Enter"))
    k=2
    t=1
    while(t<a):
        m=(2**k)-1
        n=2
        while(n<m):
            c=m%n
            n=n+1
            if (c==0):
                break
        else:
            print(m)
            t=t+1
        k=k+1
