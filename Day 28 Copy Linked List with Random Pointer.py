'''You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:



Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]
Example 2:



Input: head = [[1,null],[2,2],[3,2]]

Output: [[1,null],[2,2],[3,2]]
Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.'''

#recursion and hashmap
from typing import Optional
from xml.dom.minidom import Node


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {} #map from original node to copied node
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        if head in self.map:
            return self.map[head]
        
        copy = Node(head.val)
        self.map[head] = copy
        copy.next = self.copyRandomList(head.next) #if head.next is None, copy.next will be None, which is correct
        copy.random = self.copyRandomList(head.random) #if head.random is None, copy.random will be None, which is correct
        return copy
#time complexity: O(n)
#space complexity: O(n)

#hashmap
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict(lambda: Node(0)) #map from original node to copied node, default value is a new node with val 0
        oldToCopy[None] = None #handle edge case when head is None
        current = head
        while current:
            oldToCopy[current].val = current.val
            oldToCopy[current].next = oldToCopy[current.next] #if current.next is None, oldToCopy[current.next] will be None, which is correct
            oldToCopy[current].random = oldToCopy[current.random] #if current.random is None, oldToCopy[current.random] will be None, which is correct
            current = current.next
        return oldToCopy[head]
#time complexity: O(n)
#space complexity: O(n)

#space optimization
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random
            l1.random = l2
            l1 = l1.next

        newHead = head.random
        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None
            l1 = l1.next
        
        l1 = head
        while l1 is not None:
            l2 = l1.random
            l1.random = l2.next
            l2.next = l1.next.random if l1.next else None
            l1 = l1.next
        return newHead
#time complexity: O(n)
#space complexity: O(1)


        