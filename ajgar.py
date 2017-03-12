#My very first module========!! П-YUSH !!
#factorial(1)
def fact(Number):
    a1=Number
    f1=1
    while (a1>=2):
        f1=f1*a1
        a1=a1-1
    print(f1)
#fibonacci(2)
def fib(Number_of_terms):
    k2=Number_of_terms
    a2=-1
    b2=1
    n2=0
    while (n2<k2):
        c2=a2+b2
        print(c2)
        a2=b2
        b2=c2
        n2=n2+1

#prime or not(3)
def isprime(Number):
    a3=Number
    n3=2
    while (n3<a3):
        c3=a3%n3
        n3=n3+1
        if (c3==0):
            return("not prime")
            break
    else:
        return("prime")

#prime number
def prime(From,Till,Number=100000000000000000000):
    
    if(From==1):
        From=2
    k=0
    while(From<=Till and k<Number):
        n=2
        while(n<From):
            t=From%n
            n=n+1
            if(t==0):
                break
        else:
            print(From)
            k=k+1
        From=From+1
#nPr
def p(n,r):
    a=n
    f=1
    while(n>a-r):
        f=f*n
        n=n-1
    return(int(f))
#nCr
def c(n,r):
    a=n
    h=1
    f=1
    while (n>a-r):
        f=f*n
        n=n-1
    while (r>1):
        h=h*r
        r=r-1
    k=f/h
    return(int(k))
#Term
def t(t,x,a,n):
    r=t-1
    a=c(n,r)*(x**(n-r))*(a**r)
    print(a)
    
#Conversion of number system
def conv():
    print("This command lets you convert number system from 2 to 37")
    a=0
    while(a<=500000):
        a=a+1
    while(1>0):
        Number=input("Enter the number :")
        Number_System=int(input("Enter the number system :"))
        Convert_into=int(input("Enter the system of the required number :"))
        kiscii="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"#Thanks to Manas Kumar Verma
    #Conversion from Number_System to Decimal==================================
        Length_of_Number=len(Number)
        Counter1=1
        Answer_in_Decimal=0
        Power_of_Number_System=0
        while(Counter1<=Length_of_Number):#Thanks to Manas Kumar Verma
            Counter3=Number[-Counter1]
            Counter2=0
            while(Counter2<37):
                Counter4=kiscii[Counter2]
                if(Counter3==Counter4):
                    Value_of_corresponding_place=Counter2
                    break
                Counter2=Counter2+1
        
            if(Value_of_corresponding_place>=Number_System):
                print("Error:Number does not satisfy the condition")
                break
        
            Counter5=Value_of_corresponding_place*(Number_System**Power_of_Number_System)
            Answer_in_Decimal=Answer_in_Decimal+Counter5
            Counter1=Counter1+1
            Power_of_Number_System=Power_of_Number_System+1
    #Conversion from Decimal to Convert_into===================================
        if(Value_of_corresponding_place<Number_System):
            Output_in_reverse=""
            while(Answer_in_Decimal>0):
                Counter6=Answer_in_Decimal%Convert_into
                Answer_in_Decimal=Answer_in_Decimal//Convert_into
                Counter7=kiscii[Counter6]
                Output_in_reverse=Output_in_reverse+Counter7
            print(Output_in_reverse[::-1])
        Input_1=str(input("Exit or Retry?"))
        if(Input_1=="e"):
            break
        if(Input_1=="exit"):
            break
        if(Input_1=="Exit"):
            break
        if(Input_1=="r"):
            print("")
        if(Input_1=="retry"):
            print("")
        if(Input_1=="Retry"):
            print("")
            

    

    
