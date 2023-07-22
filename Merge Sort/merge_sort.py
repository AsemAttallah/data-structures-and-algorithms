# example=[9,8,7,6,5,4,3]
# example=[1,2,3,4,5,6,7]
example=[9,6]
def merge_sort(list):
    n=len(list)
    if n > 1 :
        mid= int(n/2)
        left=list[0:mid]
        right=list[mid:]
        # merge_sort(left)
        left.sort()
        right=list[mid:]
        # merge_sort(right)
        right.sort()
        print(left,right)
    else :
        return list
    
    i=0
    j=0
    k=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list[k]=left[i]
            i+=1
        else:
            list[k]=right[j]
            j+=1
        k+=1

        if i == len(left):
             list[k:]=right[j:]
        else:
            list[k:]=left[i:]

    return list
    
    
print(merge_sort(example))