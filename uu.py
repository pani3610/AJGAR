while(1>0):
    n=int(input("Enter number of rows"))
    import math
    s=int(math.log10(2**(n-1)))+1
    def g(a):
        k=int(math.log10(a))+1
        print((s-k)*" "+str(a),end=" ")
    for i in range(0,n):
        print(((n-1)-i)*(s+1)*" ",end="")
        for j in range(0,i+1):
            g(2**j)
        for m in range(i,0,-1):
            g(2**(m-1))
        print("")
    for i in range(n-2,-1,-1):
        print(((n-1)-i)*(s+1)*" ",end="")
        for j in range(0,i+1):
            g(2**j)
        for m in range(i,0,-1):
            g(2**(m-1))
        print("")    
    
    
        

