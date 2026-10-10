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
-100 <= Node.val <= 100
'''

#recursion
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None: #base case: if one of the lists is empty, return the other list as the merged result.
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val: #if the value of the current node in list1 is less than that of list2, we choose list1's node as the next node in the merged list.
            list1.next = self.mergeTwoLists(list1.next, list2) #call the function recursively to merge the rest of the lists, and set the next pointer of list1 to the result of that merge. This effectively builds the merged list by always choosing the smaller head node between list1 and list2.
            return list1
        else: #if the value of the current node in list2 is less than or equal to that of list1, we choose list2's node as the next node in the merged list.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
#time complexity: O(n+m)
#space complexity: O(n+m)

#iteration
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode() #create a dummy node to serve as the starting point of the merged list. This simplifies the logic for adding nodes to the merged list, as we always have a non-null node to work with.
        while list1 and list2: #while both lists have nodes to process, we compare
            if list1.val < list2.val:
                node.next = list1 #link the smaller node to the merged list, effectively adding it to the end of the merged list.
                list1 = list1.next #move the pointer of list1 to the next node, effectively removing the node we just added to the merged list from list1.
            else:
                node.next = list2 #link the smaller node to the merged list, effectively adding it to the end of the merged list.
                list2 = list2.next
            node = node.next #move the pointer of the merged list to the next node, effectively
        node.next = list1 or list2
        return dummy.next #return the next node of the dummy, which is the head of the merged list.
#time complexity: O(n+m)
#space complexity: O(1)