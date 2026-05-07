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
-1000 <= lists[i][j] <= 1000
'''

#bf
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()
        res = ListNode()
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
#time complexity: O(N log N) where N is the total number of nodes across all linked lists, due to the sorting step.
#space complexity: O(N) for storing the values of all nodes in the list before sorting.

#iteration
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
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
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next
        return res.next
#time complexity: O(N * k) where N is the total number of nodes across all linked lists and k is the number of linked lists, due to the nested loop.
#space complexity: O(1) for the iterative approach, as we are not using any additional data structures to store the nodes.