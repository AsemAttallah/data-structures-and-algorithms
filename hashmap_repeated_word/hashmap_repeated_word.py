from hashmap_repeated_word.hash_table import HashTable

def repeated_word(str):
    '''
    This function return the first repeated word in the sting
    Arguments: string
    Return: string
    '''
    str = str.split(",")
    str="".join(str).split(".")
    srt_2="".join(str)
    arr = srt_2.split(" ")
    
    hash=HashTable()
    hash.set(arr[0].capitalize(),arr[0].capitalize())
    
    i=1
    while i in range(len(arr)):
        if hash.has(arr[i].capitalize()):
            return arr[i]
        hash.set(arr[i].capitalize(),arr[i].capitalize())
        i=i+1
        
    