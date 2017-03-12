def rotate(seq):
    lst=seq[-1]
    rot=[lst]
    for i in range(len(seq)-1):
        rot.append(seq[i])
    return rot
a=[1,2,3,4,5,6]
print(rotate(a))
