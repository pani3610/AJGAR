import random
print("Multiplication Test")
w=0
while(w<1000000):
    w=w+1
print("3 chances")
w=0
while(w<1000000):
    w=w+1
print("All the best!")
w=0
while(w<450000):
    w=w+1
while(1>0):
    m=0
    n=0
    while(n<3):
        a=random.randrange(0,100)
        b=random.randrange(0,40)
        c=a*b
        s=">>"+" "+str(a)+"x"+str(b)+"="
        k=int(input(s))
        if(k==c):
            print("Correct")
            m=m+1
        else:
            print("Wrong")
            print(">>",c,"<<")
            n=n+1

    print(m,"correct")
    print(n,"wrong")
    v=str(input("Exit?"))
    if(v=="yes"):
        break
    
