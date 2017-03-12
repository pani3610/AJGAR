print("===== PRIME NUMBER OR NOT ===================================================")
while (1>0):
    a=int(input("enter the number : "))
    n=2
    while (n<a):
        c=a%n
        n=n+1
        if (c==0):
            print(a,"is a not prime number")
            break
    else:
        print(a,"is a prime number")
    print("  ")
        

        

