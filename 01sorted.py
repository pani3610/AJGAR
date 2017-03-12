listed=[]
n=int(input("Enter no of elements to be in the list > "))
a=float(input("Enter no. > "))
listed.append(a)
print(1,listed)
for i in range(1,n):
    r=0
    a=float(input("Enter no. > "))
    for j in range(len(listed)):
        
        if listed[j]>=a:
            x=listed[:j]
           
            y=listed[j:]
            
            x.append(a)
            x.extend(y)
            listed=x
            print(i+1,listed)
            break
        elif j==len(listed)-1:
            listed.append(a)
            print(i+1,listed)
            break
