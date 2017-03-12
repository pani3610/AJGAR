#HCF and LCM
a=int(input("enter first number"))
b=int(input("enter second number"))
n=1
while(n<=a and n<=b):
    c=a%n
    d=b%n
    if (c==0 and d==0):
        z=n
    n=n+1
k=int((a*b)/z)
print("HCF of",a,"and",b,"is",z)
print("LCM of",a,"and",b,"is",k)
