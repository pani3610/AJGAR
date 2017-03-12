class employee:
    e_no=0
    e_name=''
    e_designation=''
    e_address=''
    e_phno=0
    def __init__(self,values=None):
        if values==None:
            no=int(input("Enter Employee No. > "))
            name=(input("Enter Employee Name > "))
            desig=(input("Enter Employee Designation > "))
            add=(input("Enter Employee Address > "))
            phno=int(input("Enter Employee Phone No. > "))
            values=(no,name,desig,add,phno)
        self.e_no=values[0]
        self.e_name=values[1]
        self.e_designation=values[2]
        self.e_address=values[3]
        self.e_phno=values[4]
    def getdata(self):
        return (self.e_no,self.e_name,self.e_designation,self.e_address,self.e_phno)
    def putdata(self):
         print (self.e_no,self.e_name,self.e_designation,self.e_address,self.e_phno)
class salary(employee):
    basicPay=0
    DA=0
    HRA=0
    grossPay=0
    PF=0
    incomeTax=0
    netPay=0
    def getdata1(self):
        emp=self.getdata()
        if emp[2]=='Accountant':
            self.basicPay=30000
            self.grossPay=30000
            self.incomeTax=3000
        elif emp[2]=='Manager':
            self.basicPay=80000
            self.DA=10000
            self.HRA=15000
            self.grossPay=105000
            self.incomeTax=31500
        self.calculate()
    def calculate(self):
        self.netPay=self.grossPay-self.incomeTax
    def display(self):
        self.putdata()
        print(self.basicPay,self.DA,self.HRA,self.grossPay,self.PF,self.incomeTax,self.netPay)
alex=salary((1,'Alex','Manager','Street-2',1234567890))
joe=salary((2,'Joe','Accountant','Street-7',1235678990))
amit=salary((3,'Amit','Accountant','Street-6',1345567890))
alex.getdata1()
joe.getdata1()
amit.getdata1()
alex.display()
print()
joe.display()
print()
amit.display()
print()
