class distance:
    inch=0
    feet=0
    def correct(self):
        if self.inch>=12:
            self.feet+=self.inch//12
            self.inch=self.inch%12
    def add(self,distance):
        'Second distance'
        self.inch+=distance.inch
        self.feet+=distance.feet
        self.correct()
    def value(self,a,b):
        self.inch=a
        self.feet=b
        self.correct()
    def __str__(self):
        x=str(self.feet)+' feets and '+str(self.inch)+' inches'
        return x
a,b,c=distance(),distance(),distance()
x=float(input("Enter feet part of first distance > "))
y=float(input("Enter inch part of first distance > "))
z=float(input("Enter feet part of second distance > "))
w=float(input("Enter inch part of second distance > "))
a.value(y,x)
b.value(w,z)
c.value(y,x)
a.add(b)
print(c,'+',b,'=',a)
