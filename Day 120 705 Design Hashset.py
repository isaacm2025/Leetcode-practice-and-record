'''Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
Example 1:

Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]

Output: [null, null, null, true, false, null, true, null, false]
Explanation:
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1); // set = [1]
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2); // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

0 <= key <= 1,000,000
At most 10,000 calls will be made to add, remove, and contains.'''

#bf
class MyHashSet:
    def __init__(self):
        self.data = []
    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
    def contains(self, key: int) -> bool:
        return key in self.data
#time complexity: O(n) for add, remove, and contains because we are using a list to store the elements in the HashSet, which requires O(n) time to check for the presence of an element and to remove an element
#space complexity: O(n) because we are using a list to store the elements in the HashSet, which can grow up to O(n)

#using a boolean array
class MyHashSet:
    def __init__(self):
        self.data = [False] * 1000001
    def add(self, key: int) -> None:
        self.data[key] = True
    def remove(self, key: int) -> None:
        self.data[key] = False
    def contains(self, key: int) -> bool:
        return self.data[key]
#time complexity: O(1) for add, remove, and contains because we are using a boolean array to store the presence of elements in the HashSet, which allows us to access and modify the presence of an element in O(1) time
#space complexity: O(n) because we are using a boolean array of size 1000001 to store the presence of elements in the HashSet, which can grow up to O(n) where n is the maximum key value of 1000000