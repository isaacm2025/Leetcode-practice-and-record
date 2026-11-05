'''You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:



Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9'''

#iteration
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
#time complexity: O(max(n, m)) where n and m are the lengths of the two lists
#space complexity: O(max(n, m)) where n and m are the lengths of the two lists, since we are creating a new list to store the result