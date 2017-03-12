def insertionSort(seq):
    for p in range(1, len(seq)):
        while p != 0 and seq[p] < seq[p-1]:
            seq[p], seq[p-1] = seq[p-1], seq[p]
            p -= 1
            print(seq)

def selectionSort(lst):
    for i_sortpos in range(len(lst)):
        genexp = ((n, i) for i, n in enumerate(lst[i_sortpos:]))
        _, i_min = min(genexp)
        i_min += i_sortpos
        lst[i_sortpos], lst[i_min] = lst[i_min], lst[i_sortpos]
        print(lst)
a=[6,5,4,3,7,1,2]
selectionSort(a)
a=[6,5,4,3,7,1,2]
print()
insertionSort(a)
