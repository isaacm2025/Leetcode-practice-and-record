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

from typing import List, Optional
#bf
class ListNode:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()
        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
#time complexity:O(nlogn) where n is the total number of nodes across all linked lists, because we need to sort the values of all nodes.
#space complexity:O(n) where n is the total number of nodes across all linked lists, because we need to store the values of all nodes in a list before sorting and creating the merged linked list.


#iteration
class ListNode:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res
        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            if minNode == -1:
                break
            cur.next = list[minNode]
            cur = cur.next
        return res.next
#time complexity:O(nk) where n is the total number of nodes across all linked lists and k is the number of linked lists, because in the worst case, we may need to compare the heads of all k linked lists for each of the n nodes to find the minimum node.
#space complexity:O(1) because we are only using a constant amount of extra space to store the pointers and variables needed for the merging process, regardless of the number of nodes or linked lists.
