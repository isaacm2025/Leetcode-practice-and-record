'''You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import List, Optional
#brute force approach
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while list:
                nodes.append(list.val)
                lst = lst.next
        nodes.sort()
        head = ListNode(0)
        current = head
        for node in nodes:
            current.next = ListNode(node)
            current = current.next
        return head.next
#time complexity: O(nlogn) where n is the total number of nodes in all lists
#space complexity: O(n) where n is the total number of nodes in all lists


#iterative approach
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = listnode(0)
        current = res
        while True:
            min_node = -1
            for i in range(len(lists)):
                if not list[i]:
                    continue
                if min_node == -1 or list[i].val < list[min_node].val:
                    min_node = i
            if min_node == -1:
                break
            current.next = lists[min_node]
            current = current.next
            lists[min_node] = lists[min_node].next
        return res.next
#time complexity: O(nk) where n is the total number of nodes in all lists
#space complexity: O(1)