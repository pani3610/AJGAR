class timediff:
    hours=0
    minutes=0
    seconds=0
    def correct(self,t):
        if t=='val':
            if self.seconds>=60:
                self.minutes+=self.seconds//60
                self.seconds=self.seconds%60
            if self.minutes>=60:
                self.hours+=self.minutes//60
                self.minutes=self.minutes%60
        elif t=='dif':
            if self.minutes < 0:
                self.hours-=1
                self.minutes+=60
            if self.seconds < 0:
                self.minutes-=1
                self.seconds+=60
    def difference(self,time):
        'lesser time'
        self.hours-=time.hours
        self.minutes-=time.minutes
        self.seconds-=time.seconds
        self.correct('dif')
    def value(self,a,b,c):
        self.hours=a
        self.minutes=b
        self.seconds=c
        self.correct('val')
    def __str__(self):
        x=str(self.hours)+' hours '+str(self.minutes)+' minutes and '+str(self.seconds)+' seconds'
        return x
a,b,c=timediff(),timediff(),timediff()
x=int(input("Enter hours of first time > "))
y=int(input("Enter minutes of first time > "))
z=float(input("Enter seconds of first time > "))
i=int(input("Enter hours of second time > "))
j=int(input("Enter minutes of second time > "))
k=float(input("Enter seconds of second time > "))
if x>i or (x==i and y>j) or (x==i and y==j and z>=k):
    a.value(x,y,z)
    b.value(i,j,k)
    c.value(x,y,z)
else:
    a.value(i,j,k)
    b.value(x,y,z)
    c.value(i,j,k)
a.difference(b)
print('Difference betwwen',c,'and',b,'is',a)
