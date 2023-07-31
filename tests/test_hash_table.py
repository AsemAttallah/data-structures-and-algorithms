import pytest
from hash_table.hash_table import HashTable

# 1 : Setting a key/value to your hashtable results in the value being in the data structure
def test_set_to_hashtable():
    hash=HashTable()
    hash.set("a","b")
    actual = hash.get("a")
    expected = "b"
    assert actual == expected

# 2. Retrieving based on a key returns the value stored
def test_get_from_hashtable():
    hash=HashTable()
    hash.set("d","z")
    actual = hash.get("d")
    expected = "z"
    assert actual == expected

# 3. Successfully returns null for a key that does not exist in the hashtable
def test_return_none_when_no_key_exist_hashtable():
    hash=HashTable()
    hash.set("d","z")
    actual = hash.get("q")
    expected = None
    assert actual == expected
    
# 4. Successfully returns a list of all unique keys that exist in the hashtable
def test_return_all_keys_in_hashtable():
    hash=HashTable()
    hash.set("d","z")
    hash.set("a","v")
    hash.set("s","g")
    actual = hash.keys()
    expected = ['d', 'a', 's']
    assert actual == expected

# 5. Successfully handle a collision within the hashtable
def test_handle_collision():
    hash=HashTable()
    hash.set("d","z")
    hash.set("a","v")
    hash.set("s","g")
    hash.set("a","g")
    actual = hash.get_all_values_in_key("a")
    expected = ['g','v']
    assert actual == expected

# 6.Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_return_all_values_in_same_key():
    hash=HashTable()
    hash.set("d","z")
    hash.set("a","v")
    hash.set("s","g")
    hash.set("a","g")
    actual = hash.get_all_values_in_key("a")
    expected = ['g','v']
    assert actual == expected

# 7. Successfully hash a key to an in-range value
def test_hash_key_inrange():
  expected = 1024
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  actual2 = hash._HashTable__hash('a')
  actual3 = hash._HashTable__hash('s')
  assert   actual < expected
  assert   actual2 < expected
  assert   actual3 < expected


