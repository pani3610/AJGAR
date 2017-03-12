def search(List,No):
    low=0
    high=len(List)-1
    while low < high:
        mid=(low+high)//2
        if List[mid]==No:
            print("Element Found at index %s"%(mid))
            break
        if List[mid]<No:
            low=mid+1
        if List[mid]>No:
            high=mid-1
    if low>=high:
        print("Element not found")
