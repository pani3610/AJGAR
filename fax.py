
a="Green"
b="*"
n=0
while(n<=74):
    if(n>50 and n<70):
        a="Orange"
    if(n>=70 and n<=73):
        a=" Red "
    print(n*b+a+int((74-n))*b)
    n=n+1
    
    t=1
    while(t<300000):
            t=t+1
    
