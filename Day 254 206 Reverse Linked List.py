'''Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
'''

#recursion
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
#time complexity: O(n)
#space complexity: O(n)

#iteration  
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            tmp = curr.next #store the next node
            curr.next = prev #reverse the link, why? because we want to point the current node to the previous node, effectively reversing the direction of the list.
            prev = curr #move prev to current
            curr = tmp #move curr to next node
        return prev
#time complexity: O(n)
#space complexity: O(1)