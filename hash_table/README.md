# Code Challenge 30 : Hash Table

## Approach & Efficiency (for all methods)
* In this code I used a while loop to traverse to each node and if statement to make a specific conditions

* Big O for all methods:
    - O (n): Time complexity where n is the number of nodes when collision case happened
    - O (1): Time complexity when collision case does not happen
    - O (n): Space complexity where n is the number of buckets

## Solution 

## Setting a key/value to your hashtable results in the value being in the data structure
* input : hash.set("a","b")
* hash.get("a")
* output : "b"

## Retrieving based on a key returns the value stored
def test_get_from_hashtable():
* input : hash.set("d","z")
* hash.get("d")
* output : "z"
   

## Successfully returns null for a key that does not exist in the hashtable
* input : hash.set("d","z")
* hash.get("q")
* output : None
    
    
## Successfully returns a list of all unique keys that exist in the hashtable
* input : hash.set("d","z")
* hash.set("a","v")
* hash.set("s","g")
* hash.keys()
* output : ['d', 'a', 's']

## Successfully handle a collision within the hashtable
* input : hash.set("d","z")
* hash.set("a","v")
* hash.set("s","g")
* hash.set("a","g")
* hash.get_all_values_in_key("a")
* output : {'a':'g'} -> {'a':'v'} -> None

## Successfully retrieve a value from a bucket within the hashtable that has a collision
* input : hash.set("d","z")
* hash.set("a","v")
* hash.set("s","g")
* hash.set("a","g")
* hash.get_all_values_in_key("a")
* output : {'a':'g'} -> {'a':'v'} -> None
    
## Successfully hash a key to an in-range value
* hash._HashTable__hash('d') < 1024
* hash._HashTable__hash('a') < 1024
* hash._HashTable__hash('s') < 1024
