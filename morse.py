import turtle
def morse(b):        
    def tym1():
        i=0
        while(i<=2500000):
            i+=1
    def tym2():
        i=0
        while(i<=600000):
            i+=1        
    def tym3():
        i=0
        while(i<=250000):
            i+=1        

    def dot():
        turtle.bgcolor("yellow")
        turtle.dot(250,"blue")
        turtle.ht()
        tym2()
        turtle.clear()
        tym1()

    def doty():
        turtle.bgcolor("yellow")
        turtle.dot(250,"blue")
        turtle.ht()
        tym2()
        turtle.clear()
        
    def dash():
        doty()
        tym3()
        doty()
        tym3()
        dot()

    def conv(a=str()):
        for i in a:
            if(i=="."):
                dot()
            elif(i=="-"):
                dash()
            
            elif(i==" "):
                turtle.bgcolor("pink")
                tym1()
                tym1()
                
    d={" ":" ","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    
    def m(x,y):
        turtle.bye()
        turtle.ht()
        turtle.clear()
        turtle.bgcolor("yellow")
        tym1()
        t=0
        c=b+" "
        for i in str(c):
            if(t<len(b)-1 ):
                if(b[t-1]!=" " and i!=" "):
                  turtle.bgcolor("green")
                j=0
                while(j<=1500000):
                    j+=1
               
            if(i!=" " and c[t-1]!=" "):
                turtle.bgcolor("green")
                j=0
                while(j<=1500000):
                    j+=1
            conv(d[i])
            t+=1
            
        turtle.write("end",align="center",font=("Arial",35,"normal"))
        turtle.st()
        def n(x,y):
            turtle.bye()
        turtle.onclick(n)
    turtle.screensize(500,500)
    turtle.bgpic("C:\Documents and Settings\INDIAN\Desktop\morfy.GIF")
    turtle.penup()
    turtle.setpos(-37,-115)
    turtle.lt(90)
    turtle.onclick(m)
        
            
    


    
    
