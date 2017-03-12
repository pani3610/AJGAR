a=[15,-5,20,-10,10]
def insertionSort(seq):
    for p in range(1, len(seq)):
        while p != 0 and seq[p] < seq[p-1]:
            seq[p], seq[p-1] = seq[p-1], seq[p]
            p -= 1
            print(seq)
insertionSort(a)
