'''You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:



Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:



Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
Constraints:

The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100'''

#recursion
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        while cur and group < k:
            cur = cur.next
            group += 1
        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                group -= 1
            head = cur
        return head
#time complexity: O(N) where N is the number of nodes in the linked list, since we visit each node at most once.
#space complexity: O(N/k) for the recursive call stack, where N is the total number of nodes and k is the size of each group.

#iteration
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    def getKth(self, cur, k):
        while cur and k>0:
            cur = cur.next
            k -= 1
        return cur
#time complexity: O(N) where N is the number of nodes in the linked list, since we visit each node at most once.
#space complexity: O(1) for the iterative approach, as we are only using a constant amount of extra space for pointers.