import pickle
x=0
y=0
class student:
    def __init__(self,sname,sadd,sphn):
        self.sname=sname
        self.sadd=sadd
        self.sphn=sphn
        global y
        self.scode=y
        y+=1
    def printstu(self):
        print('Stu Code : %s\nStu Name : %s\nAdd : %s\nPhn : %s'%(self.scode,self.sname,self.sadd,self.sphn))

class book(student):
    def __init__(self,bname,bauth,bsub,bpublish):
        self.name=bname
        self.author=bauth
        self.sub=bsub
        self.publish=bpublish
        global x
        self.code=x
        x+=1
        self.isavailable=True
        self.borrow=None
    
        
    def Showdata(self):
        print('Book Name : %s\nAuthor : %s\nEdition : %s\nPublication : %s'%(self.name,self.author,self.edn,self.publish))

    def __str__(self):
        return('Book Code : %s\nBook Name : %s\nAuthor : %s\nEdition : %s\nPublication : %s'%(self.code,self.name,self.author,self.sub,self.publish))

def Createbook():
    while True:
        name=str(raw_input("Enter Name :"))
        auth=str(raw_input("Enter Author :"))
        sub=int(raw_input("Enter Subject :"))
        publish=str(raw_input("Enter Publisher :"))
        with open('Sdata1.dat','ab') as k:
            
            obj=book(name,auth,sub,publish)
            pickle.dump(obj,k)
        global bookdir
        bookdir=LoadB()
        z=str(raw_input("Create another book?(Y/N)"))
        if(z.upper()=='N'):
            break
def CreateStudent():
    while True:
        name=str(raw_input("Enter name"))
        add=str(raw_input("Enter name"))
        phn=int(raw_input("Enter name"))
        with open('data1.dat','ab') as k:
            obj=student(name,add,phn)
            pickle.dump(obj,k)
        global studir
        studir=LoadS()
        z=str(raw_input("Register another student?(Y/N)"))
        if(z.upper()=='N'):
            break
def LoadB():
    l=[]
    with open('Sdata1.dat','rb') as k:
        try:
            while True:
                a=pickle.load(k)
                l.append(a)
        except EOFError:
            pass
    return(l)

def LoadS():
    l=[]
    with open('data1.dat','rb') as k:
        try:
            while True:
                a=pickle.load(k)
                l.append(a)
        except EOFError:
            pass
    return(l)
bookdir=LoadB()
studir=LoadS()
def OrderBook():
    q=int(input("Enter Book Code :"))
    w=int(input("Enter Student Code :"))
    if(bookdir[q].isavailable==True):
        bookdir[q].borrow=w
        bookdir[q].isavailable=False
    else:
        ("Sorry")
    RefBook()
def ReturnBook():
    e=int(input("Enter Book Code :"))
    bookdir[e].isavailable=True
    bookdir[e].borrow=None
    RefBook()
def Searchbook():
    t=int(input("Filter using  1.Name 2.Subject 3.Publisher :"))
    print("")
    global bookdir
    if(t==1):
            d=int(input("Enter Book Name :"))
            exist=False
            for i in bookdir:
                if(i.name==d and i.isavailable==True):
                    print(i)
                    print("")
                    exist=True
                if(i.name==d and i.isavailable==False):
                    
                    print(i)
                    print("(Currently unavailable)")
                    print("")
                    exist=True
            if exist==False:
                print("Book does not exist")
            
    if(t==2):
            d=str(raw_input("Enter Book Subject :"))
            exist=False
            for i in bookdir:
                if(i.sub==d and i.isavailable==True):
                    print(i)
                    print("")
                    exist=True
                if(i.sub==d and i.isavailable==False):
                    print("Currently unavailable")
                    print(i)
                    print("")
                    exist=True
            if exist==False:
                print("Book does not exist")                                      
            
    if(t==3):
            d=str(raw_input("Enter Book Publisher :"))
            exist=False
            for i in bookdir:
                if(i.publish==d and i.isavailable==True):
                    print(i)
                    print("")
                    exist=True
                if(i.publish==d and i.isavailable==False):
                    print("Currently unavailable")
                    print(i)
                    print("")
                    exist=True
            if exist==False:
                print("Book does not exist")                                      
    f=str(raw_input("Press 'O' to order :"))
    if(f.upper()=='O'):
        OrderBook()            

def RefBook():
    global bookdir
    with open('Sdata1.dat','wb') as k:
            for i in bookdir:
                pickle.dump(i,k)

def RefStu():
    global studir
    with open('data1.dat','wb') as k:
            for i in studir:
                pickle.dump(i,k)


while True:
    print("********Welcome to BHILAI LIBRARY**********")
    print("1.Teacher Zone\n2.Student Zone\n3.About Us\n")
    u=int(input("Please Enter your option :"))
    print("")
    if(u==2):
        print "Welcome to Student Zone."
        print("1.Sign Up\n2.Search or Order for a Book\n3.Return a book\n")
        m=int(input("Please Enter your option :"))
        print("")
        if(m==1):
            CreateStudent()
        elif(m==2):
            Searchbook()
        elif(m==3):
            ReturnBook() 
        
    if(u==1):
        print "Welcome to Teacher Zone.\n " 
        print("1.Register New Book\n2.Student Details\n3.Book Details\n")
        n=int(input("Please Enter your option :"))
        print("")
        if(n==1):
            Createbook()
        
        
                
        
                
            
