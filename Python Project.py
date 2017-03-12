#PIYUSH PANIGRAHI | XI F | PRACTICAL ASSIGNMENT(Python)
import math
def z(a):#for proper spacing
    b=a
    if(b==0):
        b=1
    c=4-(int(math.log(b,10)))
    print(c*" "+str(a),end=" ")

def q1():
    c1=float(input("Enter temperature in Celsius"))
    print("Temperature in fahrenheit is",(1.8*(c1)+32))

def q2():
    a2=int(input("Enter time in minutes"))
    b2=a2%1440
    c2=a2//1440
    d2=c2//365
    e2=c2%365
    print(d2,"years",e2,"days",b2,"mins")

def q3():
    a3=float(input("Enter amount of water in kilograms"))
    b3=float(input("Enter initial absolute temperature"))
    c3=float(input("Enter final absolute temperature"))
    q=a3*(c3-b3)*4184
    print("Heat required is",q,"millijoules")

def q4():
    a4=float(input("Enter acceleration in m/s2"))
    b4=float(input("Enter take off speed in m/s"))
    print("Minimum runaway length is",((b4)**2)/2*a4,"metres")

def q5():
    a5=float(input("Enter final account value"))
    b5=float(input("Enter fixed annual interest rate"))
    c5=float(input("Enter time in years"))
    d5=a5/(1+(b5/100))**c5
    print("Initial deposit amount is",d5)

def q6(x1,y1,x2,y2,x3,y3):
    s1=((x1-x2)**2+(y1-y2)**2)**0.5
    s2=((x2-x3)**2+(y2-y3)**2)**0.5
    s3=((x3-x1)**2+(y3-y1)**2)**0.5
    s=(s1+s2+s3)/2
    area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
    print("Area of triangle is",area)

def q7():
    a7=float(input("Enter number of sides of regular polygon"))
    b7=float(input("Enter length of sides of regular polygon"))
    area=(a7*((b7)**2))/(4*math.tan((math.pi)/a7))
    print("Area of polygon is",area)

def q8(x1,y1,x2,y2):
    x1=math.radians(x1)
    x2=math.radians(x2)
    y1=math.radians(y1)
    y2=math.radians(y2)
    d=6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    return(d)                    
        
def q9():
    a=[]
    for i in range(4):
        m=float(input("Enter latitude of city"+str(i+1)))
        n=float(input("Enter longitude of city"+str(i+1)))
        a.append(m)
        a.append(n)
    def t(p,q,r):
        s=(p+q+r)/2
        return((s*(s-p)*(s-q)*(s-r))**0.5)
    x=t(q8(a[0],a[1],a[2],a[3]),q8(a[2],a[3],a[6],a[7]),q8(a[0],a[1],a[6],a[7]))
    y=t(q8(a[2],a[3],a[4],a[5]),q8(a[4],a[5],a[6],a[7]),q8(a[2],a[3],a[6],a[7]))
    print((x+y),"is the enclosed area")
        
def q10():
    a10=int(input("Enter number in decimal"))
    b10="0123456789ABCDEF"
    c10=""
    while(a10>0):
        d10=a10%16
        a10=a10//16
        e10=str(b10[d10])
        c10=c10+e10
    print("Number in hexadecimal",c10[::-1])

def q11(DD,MM,YYYY):
    if(MM==1 or MM==2):
        MM=MM+12
        YYYY=YYYY-1
    j=YYYY//100
    k=YYYY%100
    h=(DD+int(2.6*(MM+1))+k+(k//4)+(j//4)+5*j)%7
    a=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    print(a[h])
def q12():
    a12=int(input("Enter coeff of x^2"))
    b12=int(input("Enter coeff of x"))
    c12=int(input("Enter constant term"))
    d12=((b12)**2)-4*a12*c12
    if(d12>=0):
        print("Root",(-b12+(d12**0.5))/2*a12)
        if(d12>0):
            print("Root",(-b12-(d12**0.5))/2*a12)
    else:
        print("The equation has no real roots")

def q13(x13,n13):
    a13=1
    c13=0
    while(a13<=n13):
        b13=((-1)**(a13+1))*((x13)**(2*a13-1))/math.factorial(2*a13-1)
        c13=c13+b13
        a13+=1
    print("sin(",x13,") =",c13)
    
def q14(x,y):
    if(x>y):
        return(x)
    elif(x<y):
        return(y)
    
def q15a():
    b=1
    while(b<=6):
        a15=1
        while(a15<=b):
            if(a15<b):
                print(a15,end=" ")
            elif(a15==b):
                print(a15)
            a15=a15+1
        b=b+1
def q15b():
    b=6
    while(b>0):
        a15=1
        while(a15<=b):
            if(a15<b):
                print(a15,end=" ")
            elif(a15==b):
                print(a15)
            a15=a15+1
        b=b-1
      
def q15c():
    import math
    def z(a):
        c=2-(int(math.log(a,10)))
        print(c*" "+str(a),end=" ")

    for i in range(0,8):
        print((7-i)*4*" ",end="")
        for j in range(0,i+1):
            z(2**j)
        for k in range(i,0,-1):
            z(2**(k-1))
        print("")

def q16():
    import math
    def z(a):
        c=4-(int(math.log(a,10)))
        print(c*" "+str(a),end=" ")
    t=0
    n=2
    c=[]
    while(t<=100):
        a=str(n)
        if(a==a[::-1]):
            for m in range(2,n):
                if(n%m==0):
                    break
            else:
                c.append(n)
                t+=1
        n+=1
    i=0
    while(i<len(c)-1):
        for j in range(0,10):
            z(c[i])
            i=i+1
        print("")
                   
def q17(a):
    x=0
    while(a>0):
        c=a%10
        a=a//10
        x=x+c
    return(x)

def q18():
    for i in range(2,11):
        print(1/i)

def q20():
    i=2000
    while(i<2100):
        for j in range(0,10):
            if(i<2100):
                print(i,end=" ")
                i=i+4
        print("")
            
def q21():
    def prime(a):
        n=2
        while(n<=(a**(1/2))):
            c=a%n
            if(c==0):
                p=0
                break
            n=n+1
        else:
            p=1
        return(p)
    a=2
    while(a<998):
        if(prime(a)+prime(a+2)==2):
            print(a,a+2)
        a=a+1
def q22():
    def prime(a):
        n=2
        while(n<=(a**(1/2))):
            c=a%n
            if(c==0):
                p=0
                break
            n=n+1
        else:
            p=1
        return(p)
    for j in range(2,32):
        if(prime((2**j)-1)==1):
            print(j,(2**j)-1)
            
def q23(n):
    a=str(n)
    if(a==a[::-1]):
        return(True)
    else:
        return(False)                                                                                                                                                                                                                                 
def q24(x,y):
    if(x>0 and y>0 and x+(2*y)<200):
        print("Inside")
    elif(x==0 or y==0 or x+(2*y)==200):
        print("On the triangle")
    else:
        print("Outside")
def q25():
    x1=float(input("Enter x-coordinate of point1"))
    y1=float(input("Enter y-coordinate of point1"))
    x2=float(input("Enter x-coordinate of point2"))
    y2=float(input("Enter y-coordinate of point2"))
    x3=float(input("Enter x-coordinate of point3"))
    y3=float(input("Enter y-coordinate of point3"))
    if(x2==x1):
        print("not possible, line parallel to x-axis")
    else:
        m=(y2-y1)/(x2-x1)
        k=(m*x3)-y3+y1-m*x1
        if(m<0):
            k=-k
        if(k>0):
            print("right")
        elif(k==0):
            print("on the line")
        else:
            print("left")
            
        
    
    
def q26():
    for i in "Python":
        if(i!="y"):
            print(i)
def q27():
    a="Global Warming"
    b=a
    print("1)",a.find("Wa"))
    print("2)",a.replace("a","*"))
    print("3)",b[4:9])
    a="Successor"
    print("4)",a.partition("s"))
    
def q28(l=list()):
    b=0
    c=[]
    for i in range(0,len(l)):
        b=b+int(l[i])
        c.append(b)
    print(c)
        
def q29(a=list()):
    f=a+[""]
    b=[]
    c=[]
    i=0
    while(i<len(a)):
        if(type(a[i])==str):
            b.append(a[i])
            a.pop(i)
            i=0
        else:
            i+=1
    a.sort()
    k=""
    for j in range(len(b)):
        i=0
        for i in range(len(b)):
            if(b[i]>k):
                k=b[i]
        b.remove(k)
        c.append(k)
        k=""
    s=a+(c[::-1])
    f.remove("")
    if(s==f):
        return(True)
    else:
        return(False)
        
def q30():
    m1=int(input("Enter nuber of rows"))
    n1=int(input("Enter nuber of columns"))
    a1=[]
    for i in range(m1):
        b1=[]
        for j in range(n1):
            s="Enter element "+str(i+1)+"x"+str(j+1)
            k=int(input(s))
            b1.insert(j,k)
        a1.append(b1)
    for i in range(0,m1):
        for j in range(0,n1):
            if(i>j):
                a1[i][j]=0
            z(a1[i][j])
        print("")

def q31(a=list()):
    a.sort()
    i=0
    while(i<len(a)-1):
        if(a[i]==a[i+1]):
            a.pop(i+1)
            i=0
        else:
            i=i+1
    print(a) 
def q32(a=list()):
    a.sort()
    print(a[::-1])

def q33():
    m1=int(input("Enter nuber of rows"))
    n1=int(input("Enter nuber of columns"))
    a1=[]
    for i in range(m1):
        b1=[]
        for j in range(n1):
            s="Enter element "+str(i+1)+"x"+str(j+1)
            k=int(input(s))
            b1.insert(j,k)
        a1.append(b1)
    for i in range(0,m1):
        for j in range(0,n1):
            if(i==j):
                z(a1[i][j])
            else:
                z(0)
        print("")
    print("---------")
    for i in range(0,m1):
        for j in range(0,n1):
            if(i+j==n1-1):
                z(a1[i][j])
            else:
                z(0)
        print("")
#
#m1=int(input("Enter nuber of rows"))
#n1=int(input("Enter nuber of cloumns"))
#a1=[]
#for i in range(m1):
 #   b1=[]
  #  for j in range(n1):
   #     s="Enter element "+str(i+1)+"x"+str(j+1)
    #    k=int(input(s))
     #   b1.insert(j,k)
#    a1.append(b1)
#m2=int(input("Enter nuber of rows"))
#n2=int(input("Enter nuber of cloumns"))
#a2=[]
#for i in range(m2):
 #   b2=[]
  #  for j in range(n2):
   #     s="Enter element "+str(i+1)+"x"+str(j+1)
    #    k=int(input(s))
     #   b2.insert(j,k)
   # a2.append(b2)
#if(m1==m2 and n1==n2):
 #   for q in range(m1):
  #      for w in range(n1):
   #         print(int(a1[q][w])+int(a2[q][w]),end=" ")
    #    print("")
#else:
 #   print("not possible")
    
       
        
    
    
    
    
                                   
    
    
    
    



    

    

    
