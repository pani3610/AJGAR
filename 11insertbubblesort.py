#Icode,  Item,       ,Qty,Price
a=[[1,  'RAM'         ,10,1000],
   [2,  'Hard Disk'   ,3, 5000],
   [3,  'Mother Board',2, 4000],
   [4,  'Processor'   ,2,10000]]
def insertionSort(seq,index):
    for p in range(1, len(seq)):
        while p != 0 and seq[p][index] > seq[p-1][index]:
            seq[p], seq[p-1] = seq[p-1], seq[p]
            p -= 1
    return seq

def bubble_sort(seq,index):
    """Sort the mutable sequence seq in place and return it."""
    for i in reversed(range(len(seq))):
        finished = True
        for j in range(i):
            if seq[j][index] > seq[j + 1][index]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                finished = False
        if finished:
            break
    return seq
print(bubble_sort(a,3))
print(insertionSort(a,2))
