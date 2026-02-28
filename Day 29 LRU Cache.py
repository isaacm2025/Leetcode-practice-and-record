'''Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in 
O
(
1
)
O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
'''
#brute force approach
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
    
    def get(self, key: int, value = int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value 
                self.cache.append(tmp)
                return
        

    def put(self, key: int, value: int) -> None:
        self.cache.pop(0)
        self.cache.append([key, value])

#time complexity: O(n) for get and O(1) for put
#space complexity: O(n) where n is the capacity of the cache

#build in OrderedDict approach
from collections import OrderedDict

class LRUCache:

    def __int__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
#time complexity: O(1) for get and put
#space complexity: O(n) where n is the capacity of the cache
    