def mors(k,z=0.5):
    import winsound
    import time
    d={" ":" ","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
    def dot():
        winsound.Beep(1000,int(500*z))
        
    def dash():
        winsound.Beep(1000,int(1500*z))
        
    for i in k:
        for m in d[i]:
            if(m=="."):
                dot()
                time.sleep(0.5*z)
            elif(m=="-"):
                dash()
                time.sleep(0.5*z)
            elif(m==" "):
                time.sleep(2.5*z)
        time.sleep(1*z)
def game():
    l="abcdefghijklmnopqrstuvwxyz"
    import random
    while(1>0):
        k=str(input("Ready?"))
        if(k==""):
            x=""
            for i in range(4):
                r=random.randrange(0,25)
                c=l[r]
                x=x+c
            mors(x)
            a=str(input("Enter the code:"))
            if(a==x):
                print("Correct")
            elif(a=="bye"):
                print("Thanks")
                break
            else:
                print("Incorrect, the answer is",x)
        else:
            break
def intro(s):
    import time
    for i in s:
        print(i,end="")
        time.sleep(0.02)
    print("")
def game1():
    f=open("C:\\Documents and Settings\\INDIAN\\Desktop\\yes.dat","rb")
    import pickle
    l=pickle.load(f)
    import random
    intro("Welcome to the interactive tutorial of 'Morse Code'. Enter 'bye' to quit.")
    while(1>0):
        k=str(input("Ready?"))
        if(k==""):
            r=random.randrange(0,len(l))
            x=l[r]
            mors(x)
            a=str(input("Enter the code:"))
            if(a==x):
                print("Correct")
            elif(a=="bye"):
                print("Thanks")
                break
            else:
                print("Incorrect, the answer is",x)
                
        else:
            break
    f.close()
