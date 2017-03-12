#fibonacci sequence
print("===== FIBONACCI SEQUENCE ====================================================")
while (1>0):
    k=int(input("Number of terms in the sequence : "))
    a=0
    b=1
    print(a)
    print(b)
    n=2
    while (n<k):
        c=a+b
        print(c)
        a=b
        b=c
        n=n+1
    print("")
