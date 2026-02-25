'''Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#recursive approach
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next) #we recursively call the function until we reach the end of the linked list, which will be the new head of the reversed linked list
            head.next.next = head
        head.next = None
        return newHead
#time complexity O(n) where n is the number of nodes in the linked list
#space complexity O(n) for the recursive call stack

#iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next #we store the next node in a temporary variable
            curr.next = prev #we reverse the current node's pointer to point to the previous node
            prev = curr #we move the previous pointer to the current node
            curr = temp #we move the current pointer to the next node
        return prev #at the end of the loop, the previous pointer will be pointing to the new head of the reversed linked list
#time complexity O(n) where n is the number of nodes in the linked list
#space complexity O(1) for the iterative approach


