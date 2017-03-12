#Reverse the number
a=int(input("enter the number"))
z=a
import math
d=int(math.log(a,10))
x=0
while (a>0):
    c=a%10
    
    a=a//10
    x=x+(c*(10**d))
    d=d-1
print("The reverse of",z,"is",x)
