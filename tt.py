import random
a=" □ "
b=" ● "
c=" X "
e="|"
l=[['1','1'],['1','2'],['1','3'],['2','1'],['2','2'],['2','3'],['3','1'],['3','2'],['3','3']]

print("Welcome to Tic-Tac-Toe")
k=[[a,a,a],[a,a,a],[a,a,a]]
print("  1   2   3")
for i in range(3):
    print(i+1,end="")
    for j in range(3):
        print(k[i][j],end="")
        if(j<2):
            print(e,end="")         
    print("")
    if(i<2):
        print(" ---┼---┼---")
v=0
for q in range(9):
    if(q%2==0):
        print("\nPlayer 1\n")
        g=tuple(input("Enter Position: "))
        k[int(g[1])-1][int(g[0])-1]=b
    else:
        print("\nPlayer 2\n")
        h=tuple(input("Enter Position: "))
        k[int(h[1])-1][int(h[0])-1]=c
    print("  1   2   3")
    for i in range(3):
        print(i+1,end="")
        for j in range(3):
            print(k[i][j],end="")
            if(j<2):
                print(e,end="")         
        print("")
        if(i<2):
            print(" ---┼---┼---")
    for m in range(3):
        if(k[m][0]==b or k[m][0]==c): 
            if (k[m][0]==k[m][1] and k[m][1]==k[m][2]):
                if(k[m][0]==b):
                    print("Player 1 wins")
                elif(k[m][0]==c):
                    print("Player 2 wins")
                v=1
                break
                
    for n in range(3):
        if(k[0][n]==b or k[0][n]==c): 
            if (k[0][n]==k[1][n] and k[1][n]==k[2][n]):
                if(k[0][n]==b):
                    print("Player 1 wins")
                elif(k[0][n]==c):
                    print("Player 2 wins")
            v=1
            break
                
    if(k[0][n]==b or k[0][n]==c):
        if(k[0][0]==k[1][1] and k[1][1]==k[2][2]):
            if(k[0][0]==b):
                    print("Player 1 wins")
            elif(k[0][n]==c):
                    print("Player 2 wins")
            v=1
            break
            
        if(k[2][0]==k[1][1] and k[1][1]==k[0][2]):
            if(k[0][n]==b):
                    print("Player 1 wins")
            elif(k[0][n]==c):
                print("Player 2 wins")
            v=1
            break
    if(v==1):
        break
if(v==0):
    print("Its a draw!")            



            
            
        




