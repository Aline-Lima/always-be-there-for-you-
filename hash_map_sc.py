# Name: Aline Lindholm Lima Botti
# OSU Email: lindhola@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 08/15
# Description: Implementation of HashMap OA

from a6_include import (DynamicArray, LinkedList, hash_function_1,
                        hash_function_2)


class HashMap:

  def __init__(self,
               capacity: int = 11,
               function: callable = hash_function_1) -> None:
    """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    self._buckets = DynamicArray()

    # capacity must be a prime number
    self._capacity = self._next_prime(capacity)
    for _ in range(self._capacity):
      self._buckets.append(LinkedList())

    self._hash_function = function
    self._size = 0

  def __str__(self) -> str:
    """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    out = ''
    for i in range(self._buckets.length()):
      out += str(i) + ': ' + str(self._buckets[i]) + '\n'
    return out

  def _next_prime(self, capacity: int) -> int:
    """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    if capacity % 2 == 0:
      capacity += 1

    while not self._is_prime(capacity):
      capacity += 2

    return capacity

  @staticmethod
  def _is_prime(capacity: int) -> bool:
    """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    if capacity == 2 or capacity == 3:
      return True

    if capacity == 1 or capacity % 2 == 0:
      return False

    factor = 3
    while factor**2 <= capacity:
      if capacity % factor == 0:
        return False
      factor += 2

    return True

  def get_size(self) -> int:
    """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    return self._size

  def get_capacity(self) -> int:
    """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
    return self._capacity

  # ------------------------------------------------------------------ #

  def put(self, key: str, value: object) -> None:
    """
        This method updates the key/value pair in the hash map. If the given key already exists in
the hash map, its associated value must be replaced with the new value. If the given key is
not in the hash map, a new key/value pair must be added.
For this hash map implementation, the table must be resized to double its current
capacity when this method is called and the current load factor of the table is
greater than or equal to 1.0.
        """
    if self.table_load() >= 1:
      self.resize_table(self._capacity * 2)
    #find out which bucket the data will go to using a hash function
    dest = self._hash_function(key) % self._capacity
    list = self._buckets[dest]
    for item in list:
      #if it already exists in the hashmap, override previous value with new value
      if item.key == key:
        item.value = value
        return
    #if we get to this point, key was not found, so we can insert into list
    list.insert(key, value)
    self._size += 1

  def empty_buckets(self) -> int:
    """
        This method returns the number of empty buckets in the hash table
        """
    output = 0
    for i in range(self._capacity):
      if self._buckets[i].length() == 0:
        output += 1
    return output

  def table_load(self) -> float:
    """
        This method returns the current hash table load factor (percentage full)
        """
    #calculate number of elements and divide by the capacity
    return self._size / self._capacity

  def clear(self) -> None:
    """
        This method clears the contents of the hash map. It does not change the underlying hash
table capacity.
        """
    for i in range(self._capacity):
      self._buckets[i] = LinkedList()

    self._size = 0

  def resize_table(self, new_capacity: int) -> None:
    """
        This method changes the capacity of the internal hash table. All existing key/value pairs
must remain in the new hash map, and all hash table links must be rehashed. (Consider
calling another HashMap method for this part).
First check that new_capacity is not less than 1; if so, the method does nothing.
If new_capacity is 1 or more, make sure it is a prime number. If not, change it to the next
highest prime number. You may use the methods _is_prime() and _next_prime() from the
skeleton code.
        """
    if new_capacity < 1:
      return
    elif not self._is_prime(new_capacity):
      new_capacity = self._next_prime(new_capacity)

    #create a new hashmap of new capacity
    temp = DynamicArray()
    for i in range(new_capacity):
      temp.append(LinkedList())

    #stored old buckets in a separate variable, and add new set of buckets in
    extra = self._buckets
    prevCap = self._capacity
    self._capacity = new_capacity
    self._buckets = temp
    self._size = 0

    #go through previous buckets and insert into new buckets
    for i in range(prevCap):
      for item in extra[i]:
        self.put(item.key, item.value)

  def get(self, key: str):
    """
        This method returns the value associated with the given key. If the key is not in the hash
map, the method returns None.
        """
    #All other methods can use the following hints:
    #In order find something with a key, you need to use the hash function to find the bucket it should be in, and then iterate through the linked list until you find the key.
    #This linked list doesn't have an iterator, so you just need to travel down using .next and compar that nodes key
    #once you find the key, return the value of the node and you're good
    dest = self._hash_function(key) % self._capacity
    list = self._buckets[dest]
    output = list.contains(key)
    if output:
      return output.value
    else:
      return None

  def contains_key(self, key: str) -> bool:
    """
        This method returns True if the given key is in the hash map, otherwise it returns False. An
empty hash map does not contain any keys.
        """
    #contains key is similar to the hints for get, but instead of returning the value, you return True
    dest = self._hash_function(key) % self._capacity
    list = self._buckets[dest]
    return list.contains(key) != None

  def remove(self, key: str) -> None:
    """
        This method removes the given key and its associated value from the hash map. If the key
is not in the hash map, the method does nothing (no exception needs to be raised).
        """
    #This method uses the same hints, but instead of returning anything, you need to manage the nodes in a way that the previous node.next = current node.next, effectively jumping over the node
    dest = self._hash_function(key) % self._capacity
    list = self._buckets[dest]
    if list.remove(key):
        self._size-=1

  def get_keys_and_values(self) -> DynamicArray:
    """
        This method returns a dynamic array where each index contains a tuple of a key/value pair
stored in the hash map. The order of the keys in the dynamic array does not matter.
        """
    #this is tedious, but not miserable. Effectively iterate through them with a dynamic array (list) that stores the key value pair as (key,value). This will use a for loop like we did for some other methods, followed by the node iteration for the .get, .contains_key, and .remove methods.
    output = DynamicArray()
    for i in range(self._buckets.length()):
      bucket = self._buckets[i]
      for item in bucket:
        output.append((item.key, item.value))

    return output


def find_mode(da: DynamicArray) -> (DynamicArray, int):
  # 15 points
  """
    Write a standalone function outside of the HashMap class that receives a dynamic array
(that is not guaranteed to be sorted). This function will return a tuple containing, in this
order, a dynamic array comprising the mode (most occurring) value/s of the array, and an
integer that represents the highest frequency (how many times the mode value(s) appear).
If there is more than one value with the highest frequency, all values at that frequency
should be included in the array being returned (the order does not matter). If there is only
one mode, the dynamic array will only contain that value.
You may assume that the input array will contain at least one element, and that all values
stored in the array will be strings. You do not need to write checks for these conditions.
For full credit, the function must be implemented with O(N) time complexity. For best
results, we recommend using the separate chaining hash map provided for you in the
function’s skeleton code.
    """
  # if you'd like to use a hash map,
  # use this instance of your Separate Chaining HashMap
  map = HashMap()
  arr = DynamicArray()
  max = 0
  #populate the hashMap
  for i in range(da.length()):
    if map.contains_key(da[i]):
      map.put(da[i], map.get(da[i]) + 1)
    else:
      map.put(da[i], 1)
  #go through and find key with highest value

  set = map.get_keys_and_values()
  print(set)
  for i in range(set.length()):
    if (set[i][1] > max):
      max = set[i][1]

  for i in range(set.length()):
    if (set[i][1] == max):
      arr.append(set[i][0])

  return (arr, max)


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

  print("\nPDF - put example 1")
  print("-------------------")
  m = HashMap(53, hash_function_1)
  for i in range(150):
    m.put('str' + str(i), i * 100)
    if i % 25 == 24:
      print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(),
            m.get_capacity())

  print("\nPDF - put example 2")
  print("-------------------")
  m = HashMap(41, hash_function_2)
  for i in range(50):
    m.put('str' + str(i // 3), i * 100)
    if i % 10 == 9:
      print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(),
            m.get_capacity())

  print("\nPDF - empty_buckets example 1")
  print("-----------------------------")
  m = HashMap(101, hash_function_1)
  print(m.empty_buckets(), m.get_size(), m.get_capacity())
  m.put('key1', 10)
  print(m.empty_buckets(), m.get_size(), m.get_capacity())
  m.put('key2', 20)
  print(m.empty_buckets(), m.get_size(), m.get_capacity())
  m.put('key1', 30)
  print(m.empty_buckets(), m.get_size(), m.get_capacity())
  m.put('key4', 40)
  print(m.empty_buckets(), m.get_size(), m.get_capacity())

  print("\nPDF - empty_buckets example 2")
  print("-----------------------------")
  m = HashMap(53, hash_function_1)
  for i in range(150):
    m.put('key' + str(i), i * 100)
    if i % 30 == 0:
      print(m.empty_buckets(), m.get_size(), m.get_capacity())

  print("\nPDF - table_load example 1")
  print("--------------------------")
  m = HashMap(101, hash_function_1)
  print(round(m.table_load(), 2))
  m.put('key1', 10)
  print(round(m.table_load(), 2))
  m.put('key2', 20)
  print(round(m.table_load(), 2))
  m.put('key1', 30)
  print(round(m.table_load(), 2))

  print("\nPDF - table_load example 2")
  print("--------------------------")
  m = HashMap(53, hash_function_1)
  for i in range(50):
    m.put('key' + str(i), i * 100)
    if i % 10 == 0:
      print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

  print("\nPDF - clear example 1")
  print("---------------------")
  m = HashMap(101, hash_function_1)
  print(m.get_size(), m.get_capacity())
  m.put('key1', 10)
  m.put('key2', 20)
  m.put('key1', 30)
  print(m.get_size(), m.get_capacity())
  m.clear()
  print(m.get_size(), m.get_capacity())

  print("\nPDF - clear example 2")
  print("---------------------")
  m = HashMap(53, hash_function_1)
  print(m.get_size(), m.get_capacity())
  m.put('key1', 10)
  print(m.get_size(), m.get_capacity())
  m.put('key2', 20)
  print(m.get_size(), m.get_capacity())
  m.resize_table(100)
  print(m.get_size(), m.get_capacity())
  m.clear()
  print(m.get_size(), m.get_capacity())

  print("\nPDF - resize example 1")
  print("----------------------")
  m = HashMap(23, hash_function_1)
  m.put('key1', 10)
  print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
  m.resize_table(30)
  print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

  print("\nPDF - resize example 2")
  print("----------------------")
  m = HashMap(79, hash_function_2)
  keys = [i for i in range(1, 1000, 13)]
  for key in keys:
    m.put(str(key), key * 42)
  print(m.get_size(), m.get_capacity())

  for capacity in range(111, 1000, 117):
    m.resize_table(capacity)

    m.put('some key', 'some value')
    result = m.contains_key('some key')
    m.remove('some key')

    for key in keys:
      # all inserted keys must be present
      result &= m.contains_key(str(key))
      # NOT inserted keys must be absent
      result &= not m.contains_key(str(key + 1))
    print(capacity, result, m.get_size(), m.get_capacity(),
          round(m.table_load(), 2))

  print("\nPDF - get example 1")
  print("-------------------")
  m = HashMap(31, hash_function_1)
  print(m.get('key'))
  m.put('key1', 10)
  print(m.get('key1'))

  print("\nPDF - get example 2")
  print("-------------------")
  m = HashMap(151, hash_function_2)
  for i in range(200, 300, 7):
    m.put(str(i), i * 10)
  print(m.get_size(), m.get_capacity())
  for i in range(200, 300, 21):
    print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

  print("\nPDF - contains_key example 1")
  print("----------------------------")
  m = HashMap(53, hash_function_1)
  print(m.contains_key('key1'))
  m.put('key1', 10)
  m.put('key2', 20)
  m.put('key3', 30)
  print(m.contains_key('key1'))
  print(m.contains_key('key4'))
  print(m.contains_key('key2'))
  print(m.contains_key('key3'))
  m.remove('key3')
  print(m.contains_key('key3'))

  print("\nPDF - contains_key example 2")
  print("----------------------------")
  m = HashMap(79, hash_function_2)
  keys = [i for i in range(1, 1000, 20)]
  for key in keys:
    m.put(str(key), key * 42)
  print(m.get_size(), m.get_capacity())
  result = True
  for key in keys:
    # all inserted keys must be present
    result &= m.contains_key(str(key))
    # NOT inserted keys must be absent
    result &= not m.contains_key(str(key + 1))
  print(result)

  print("\nPDF - remove example 1")
  print("----------------------")
  m = HashMap(53, hash_function_1)
  print(m.get('key1'))
  m.put('key1', 10)
  print(m.get('key1'))
  m.remove('key1')
  print(m.get('key1'))
  m.remove('key4')

  print("\nPDF - get_keys_and_values example 1")
  print("------------------------")
  m = HashMap(11, hash_function_2)
  for i in range(1, 6):
    m.put(str(i), str(i * 10))
  print(m.get_keys_and_values())

  m.put('20', '200')
  m.remove('1')
  m.resize_table(2)
  print(m.get_keys_and_values())

  print("\nPDF - find_mode example 1")
  print("-----------------------------")
  da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
  mode, frequency = find_mode(da)
  print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

  print("\nPDF - find_mode example 2")
  print("-----------------------------")
  test_cases = ([
    "Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu",
    "Ubuntu"
  ], ["one", "two", "three", "four", "five"], [
    "2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"
  ])

  for case in test_cases:
    da = DynamicArray(case)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
