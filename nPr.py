n=int(input("enter n of nPr : "))
r=int(input("enter r of nPr : "))
a=n
f=1
while (n>a-r):
    f=f*n
    n=n-1
print(a,"P",r,"is ",f)
