def insertion(arr):
    '''
    This function make an insertion sort  
    '''
    sorted_arr=arr
    for i in range(len(arr)):
        if i<len(arr)-1:
            # print(sorted_arr)
            if sorted_arr[i]>sorted_arr[i+1]:
                value_large=sorted_arr[i]
                value_small=sorted_arr[i+1]
                sorted_arr[i+1]=value_large
                sorted_arr.pop(i)
                for j in range(len(sorted_arr)):
                    if value_small<sorted_arr[j]:
                        sorted_arr.insert(j,value_small)
                        break
    return sorted_arr

reverse_sorted = [20,18,12,8,5,-2]
few_uniques = [5,12,7,5,5,7]
nearly_sorted = [2,3,5,7,13,11]
    

print(insertion(nearly_sorted))