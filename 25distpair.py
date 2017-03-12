a=[]
for i in range(10):
    x,y=eval(input("Enter x,y > "))
    
    a.append((x,y))
x=float('inf')
b=[]
for i in range(11):
    for j in range(i+1,11):
        d=((((a[j][0]-a[i][0])**2)+((a[j][1]-a[i][1])**2))**(1/2))
        if d < x:
            x=d
            b=[[a[i][0],a[i][1]],[a[j][0],a[j][1]]]
print(b)
