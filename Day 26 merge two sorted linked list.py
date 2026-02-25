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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#recursive approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2) #we recursively call the function with the next node of list1 and the current node of list2
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next) #we recursively call the function with the current node of list1 and the next node of list2
            return list2
#time complexity O(n+m) where n and m are the number of nodes in list1 and list2 respectively
#space complexity O(n+m) for the recursive call stack

#iterative approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() #we create a dummy node to simplify the merging process
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next #we move the node pointer to the next node in the merged list
        node.next = list1 or list2 #we append the remaining nodes of list1 or list2 to the merged list
        return dummy.next #we return the next node of the dummy node, which is the head of the merged list
#time complexity O(n+m) where n and m are the number of nodes in list1 and list2 respectively
#space complexity O(1) for the iterative approach