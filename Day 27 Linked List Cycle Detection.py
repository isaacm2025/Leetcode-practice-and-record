'''Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:



Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:



Input: head = [1,2], index = -1

Output: false
Constraints:

0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
#hash set

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #to store the nodes we have seen so far
        cur = head #to traverse the linked list
        while cur:
            if cur in seen: #if we have seen this node before, then there is a cycle
                return True
            seen.add(cur) #add the current node to the set of seen nodes
            cur = cur.next #move to the next node
        return False
#time complexity: O(n)
#space complexity: O(n)

#two pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head #slow pointer
        fast = head #fast pointer
        while fast and fast.next: #while fast pointer is not null and fast pointer's next
            slow = slow.next #move slow pointer by 1
            fast = fast.next.next #move fast pointer by 2
            if slow == fast: #if slow pointer and fast pointer are the same, then there is a cycle
                return True
        return False
#time complexity: O(n)
#space complexity: O(1)
