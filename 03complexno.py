class complexNo:
    real=0
    imaginary=0
    def add(self,complexno):
        'Second complex no'
        self.real+=complexno.real
        self.imaginary+=complexno.imaginary
    def value(self,a,b):
        'a,b <- a+bi'
        self.real=a
        self.imaginary=b
    def __str__(self):
        x=str(self.real)+'+'+str(self.imaginary)+'i'
        return x
a,b,c=complexNo(),complexNo(),complexNo()
x=float(input("Enter real part of first complex no. > "))
y=float(input("Enter imaginary part of first complex no. > "))
z=float(input("Enter real part of second complex no. > "))
w=float(input("Enter imaginary part of second complex no. > "))
a.value(x,y)
b.value(z,w)
c.value(x,y)
a.add(b)
print(c)
print(c,'+',b,'=',a)
