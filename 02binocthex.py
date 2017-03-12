accuracy=10
n=float(input("Enter a no. > "))
t=input("Convert to (B)inary , (O)ctal or (H)exadecimal > ")
if t.lower().startswith('b'):
    b=2
elif t.lower().startswith('o'):
    b=8
elif t.lower().startswith('h'):
    b=16
nint=int(n//1)
nflt=n%1
x=""
y=""
while True:
    if int(nint%b) <= 9:
        x=x+str(int(nint%b))
    if int(nint%b) > 9 :
        h=(int(nint%b)-9)
        x=x+chr(64+h)
    nint=nint//b
    if nint == 0:
        break
while True:
    if int((nflt*b)//1) <= 9:
        y=y+str(int((nflt*b)//1))
    if int((nflt*b)//1) > 9:
        h=(int((nflt*b)//1)-9)
        y=y+chr(64+h)
    nflt=(nflt*b)%1
    if nflt==0 or len(y)>=accuracy:
        break
print("The %s value of number is"%{2:'binary',8:'octal',16:'hexadecimal'}[b],x[::-1]+"."+y)
