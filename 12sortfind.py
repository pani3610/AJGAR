a=[15,-5,20,-10,10]
x=0
def insertionSort(seq):
    for p in range(1, len(seq)):
        while p != 0 and seq[p] < seq[p-1]:
            seq[p], seq[p-1] = seq[p-1], seq[p]
            p -= 1
    return seq

a=(input("Enter a List > "))
b=float(input("Enter a no. > "))
a=insertionSort(a)
for i in range(len(a)):
    if a[i]==b:
        x=[i]
        break
if x==0:
    print('No. not found')
else:
    print("No. found at index",x[0])
