k=int(input("Enter how many"))
print(2)
a=3
d=0
while(d<k-1): 
    n=2
    while (n<a):
        c=a%n
        n=n+1
        if (c==0):
            
            break
    else:
        print(a)
        d=d+1
    a=a+1
