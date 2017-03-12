#guess the number
print("Guess the number between 0 to 1000 in 9 tries")
import random
while(1>0):
    n=9
    f=random.randrange(0,1000)
    while(n>-1):
        a=int(input("Guess the number :"))
        if(a==f):
            print("You did it!")
            break
        if(a<f):
            if(n>0):
                print("Its greater than",a)
                if(n>1):
                    k="tries"
                else:
                    k="try"
                print("You have",n,k,"left")
            print("")
            n=n-1
        if(a>f):
            if(n>0):
                print("Its less than",a)
                if(n>1):
                    k="tries"
                else:
                    k="try"
                print("You have",n,k,"left")
            print("")
            n=n-1
    print("")
    print("The number is",f)
    print("Thanks for playing")
