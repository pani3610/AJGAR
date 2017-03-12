def muz(l,a=2,b=0.5):
    import winsound
    i=0
    while(i<len(l)):
        if(l[i]=="s"):
            winsound.Beep(a*240,int(b*800))
        elif(l[i]=="r"):
            winsound.Beep(a*270,int(b*800))
        elif(l[i]=="g"):
            winsound.Beep(a*300,int(b*800))
        elif(l[i]=="m"):
            winsound.Beep(a*320,int(b*800))
        elif(l[i]=="p"):
            winsound.Beep(a*360,int(b*800))
        elif(l[i]=="d"):
            winsound.Beep(a*400,int(b*800))
        elif(l[i]=="n"):
            winsound.Beep(a*450,int(b*800))
        elif(l[i]=="S"):
            winsound.Beep(a*480,int(b*800))
        elif(l[i]=="R"):
            winsound.Beep(a*540,int(b*800))
        elif(l[i]=="G"):
            winsound.Beep(a*600,int(b*800))    
        elif(l[i]=="k"):
            if(i!=len(l)-1):
                if(l[i+1]=="r"):
                    winsound.Beep(a*256,int(b*800))
                    i+=1
                elif(l[i+1]=="g"):
                    winsound.Beep(a*288,int(b*800))    
                    i+=1
                elif(l[i+1]=="m"):
                    winsound.Beep(a*337,int(b*800))
                    i+=1
                elif(l[i+1]=="d"):
                    winsound.Beep(a*384,int(b*800))
                    i+=1
                elif(l[i+1]=="n"):
                    winsound.Beep(a*432,int(b*800))
                    i+=1
                elif(l[i+1]=="R"):
                    winsound.Beep(a*512,int(b*800))
                    i+=1
                elif(l[i+1]=="G"):
                    winsound.Beep(a*576,int(b*800))
                    i+=1
        i+=1
while(1>0):
    import random
    a=["s","r","g","m","p","d","n","S","k"]
    x=""
    for i in range(8):
        b=random.randrange(0,9)
        c=a[b]
        x=x+c
    print(x)
    muz(x,2,0.5)
    
    
            
