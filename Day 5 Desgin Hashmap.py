'''Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
Example 1:

Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output: [null, null, null, 1, -1, null, 1, null, -1]
Explanation:
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1); // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3); // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2); // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2); // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:

0 <= key, value <= 1,000,000
At most 10,000 calls will be made to put, get, and remove.'''

#Array
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001  # Initialize an array of size 1,000,001 with all values set to -1

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

    
#time complexity O(1) for each function call
#space complexity O(1000000) since the key is in the range 0 to 1,000,000


#linked list approach

'''To reduce memory usage, we use a hash table with separate chaining. 
We create an array of buckets (smaller than the key range) and use a hash function (key modulo bucket count) to determine which bucket a key belongs to. 
Each bucket is a linked list that stores key-value pairs. This handles collisions by chaining multiple entries in the same bucket.

'''

class ListNode:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None    
class MyHashMap:
    
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [None] * self.bucket_count

    def _hash(self, key: int) -> int:
        return key % self.bucket_count

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(-1, -1)  # Dummy head

        prev = self._find(self.buckets[index], key)
        if prev.next:
            prev.next.value = value  # Update existing value
        else:
            prev.next = ListNode(key, value)  # Insert new key-value pair

    def get(self, key: int) -> int:
        index = self._hash(key)
        if not self.buckets[index]:
            return -1

        prev = self._find(self.buckets[index], key)
        if prev.next:
            return prev.next.value
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            return

        prev = self._find(self.buckets[index], key)
        if prev.next:
            prev.next = prev.next.next  # Remove the node

    def _find(self, head: ListNode, key: int) -> ListNode:
        prev = head
        curr = head.next
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev
#time complexity O(N/K) for each function call where N is number of all possible keys and K is number of buckets
#space complexity O(K + M) where K is number of buckets and M is number of unique keys inserted into the hashmap