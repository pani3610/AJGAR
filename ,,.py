m1=int(input("Enter nuber of rows"))
n1=int(input("Enter nuber of cloumns"))
a1=[]
for i in range(m1):
    b1=[]
    for j in range(n1):
        s="Enter element "+str(i+1)+"x"+str(j+1)
        k=int(input(s))
        b1.insert(j,k)
    a1.append(b1)
m2=int(input("Enter nuber of rows"))
n2=int(input("Enter nuber of cloumns"))
a2=[]
for i in range(m2):
    b2=[]
    for j in range(n2):
        s="Enter element "+str(i+1)+"x"+str(j+1)
        k=int(input(s))
        b2.insert(j,k)
    a2.append(b2)
if(m1==m2 and n1==n2):
    for q in range(m1):
        for w in range(n1):
            print(int(a1[q][w])+int(a2[q][w]),end=" ")
        print("")
else:
    print("not possible")
    
       
        
    
