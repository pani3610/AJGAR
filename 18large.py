matrix=[]
m=int(input("Enter no of rows > "))
n=int(input("Enter no of columns > "))
for i in range(m):
  x=[]
  for j in range(n):
    x.append(int(input("Enter "+str(i+1)+' , '+str(j+1)+' element : ')))
  matrix.append(x)
a=[]
for i in range(len(matrix)):
  x=[0,0]
  for j in range(len(matrix[i])):
    if matrix[i][j]>x[0]:
      x=[matrix[i][j],j]
  a.append(x)
x=[[0,0],0]
for i in range(len(a)):
  if a[i][0]>x[0][0]:
    x=[a[i],i]
print("Largest element is at",x[1]+1,',',x[0][1]+1)
