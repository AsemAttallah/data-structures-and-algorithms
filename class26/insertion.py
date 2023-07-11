reverse_sorted = [20,18,12,8,5,-2]
few_uniques = [5,12,7,5,5,7]
nearly_sorted = [2,3,5,7,13,11]

def insertion(arr):
    sorted_arr=[arr[0]]
    for i in range(len(arr)-1):
        if arr[i+1]>sorted_arr[i]:
            sorted_arr.append(arr[i+1])
        elif arr[i+1]<sorted_arr[i]:
            sorted_arr.insert(0,arr[i+1])
    return sorted_arr
        

    

print(insertion(reverse_sorted))