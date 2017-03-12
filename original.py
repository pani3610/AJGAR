def conv(a,v,g=10):
    kiscii="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k=len(a)
    z=1
    x=0
    m=0
    while(z<=k):
        c=a[-z]
        n=0
        while(n<37):
            h=kiscii[n]
            if(c==h):
                s=n
                break
            n=n+1
        
        if(s>=v):
            print("Error:Number does not satisfy the condition")
            break
        
        t=s*(v**m)
        x=x+t
        z=z+1
        m=m+1
    if(s<v):
        d=""
        while(x>0):
            q=x%g
            x=x//g
            w=kiscii[q]
            d=d+w
        print(d[::-1])
