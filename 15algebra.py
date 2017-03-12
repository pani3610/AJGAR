class LinearEquation:
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    def get_a(self):
        self.a=float(input("Enter a > "))
    def get_b(self):
        self.b=float(input("Enter b > "))
    def get_c(self):
        self.c=float(input("Enter c > "))
    def get_d(self):
        self.d=float(input("Enter d > "))
    def get_e(self):
        self.e=float(input("Enter e > "))
    def get_f(self):
        self.f=float(input("Enter f > "))
    def getX(self):
        if self.isSolvable():
            print(((self.e*self.d)-(self.b*self.f))/((self.a*self.d)-(self.b*self.c)))
        else:
            print("Equation has no solution")
    def getY(self):
        if self.isSolvable():
            print(((self.a*self.f)-(self.e*self.c))/((self.a*self.d)-(self.b*self.c)))
        else:
            print("Equation has no solution")
    def isSolvable(self):
        if ((self.a*self.d)-(self.b*self.c))  !=0:
            return True
        else:
            return False

le=LinearEquation()
print("for equations:\na*x+b*y=e and\nc*x+d*y=f")
le.get_a()
le.get_b()
le.get_c()
le.get_d()
le.get_e()
le.get_f()
le.getX()
le.getY()
