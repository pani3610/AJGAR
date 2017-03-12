def line_intersect(line_1,line_2):
    l1,l2=line_1,line_2
    m1=(l1[1][1]-l1[0][1])/(l1[1][0]-l1[0][0])
    m2=(l2[1][1]-l2[0][1])/(l2[1][0]-l2[0][0])
    c1=-m1*l1[0][0]+l1[0][1]
    c2=-m2*l2[0][0]+l2[0][1]
    if m1==m2 and c1==c2:
        return l1
    elif m1!=m2:
        a=[[-m1,1],[-m2,1]]
        b=[[c1],[c2]]
        deta=1/((a[1][1]*a[0][0])-(a[0][1]*a[1][0]))
        ainv=[[a[1][1]*deta,-a[0][1]*deta],[-a[1][0]*deta,a[0][0]*deta]]

        result = [0,0]

        for i in range(len(a)):
           for j in range(len(b[0])):
               for k in range(len(b)):
                   result[i] += a[i][k] * b[k][j]

        
        return result 
    else:
        return None
