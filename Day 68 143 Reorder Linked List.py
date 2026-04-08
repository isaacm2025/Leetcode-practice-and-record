'''You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000'''

#brute force
from logging import root
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j :
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None
#time complexity: O(n) where n is the length of the linked list
#space complexity: O(n) where n is the length of the linked list

#rercursion
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(root: ListNode, cur: ListNode) -> ListNode:
            if not head:
                return root
            root = rec(root, cur.next)
            if not root:
                return None
            tmp = None
            if root == cur or root.next == cur:
                tmp = root.next
                root.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp
        head = rec(head, head.next)
#time complexity: O(n) where n is the length of the linked list
#space complexity: O(n) where n is the length of the linked list due to recursion


#reverse and merge
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next =second
            second.next = tmp1
            first, second = tmp1, tmp2
#time complexity: O(n) where n is the length of the linked list
#space complexity: O(1)