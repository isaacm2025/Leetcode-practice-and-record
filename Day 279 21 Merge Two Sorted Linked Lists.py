'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100'''

#recursion
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2) # Recursively merge the rest of the lists, self.mergeTwoLists(list1.next, list2) will return the head of the merged list of the remaining nodes, call the function again with the next node of list1 and the current node of list2
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next) # Recursively merge the rest of the lists, self.mergeTwoLists(list1, list2.next) will return the head of the merged list of the remaining nodes, call the function again with the current node of list1 and the next node of list2
            return list2
#time complexity: O(n + m) where n and m are the lengths of the two lists
#space complexity: O(n + m) due to the recursion stack

#iteration
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 # If the value of the current node in list1 is less than the value of the current node in list2, we set the next pointer of the current node in the merged list to point to the current node in list1. This effectively adds the current node from list1 to the merged list.
                list1 = list1.next # We then move the pointer in list1 to the next node, so that we can continue comparing the next nodes in the next iteration of the loop.
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2 # If one of the lists is not empty, we can simply append the remaining nodes to the merged list. This is because both lists are already sorted
        return dummy.next
#O(n + m) time complexity, O(1) space complexity