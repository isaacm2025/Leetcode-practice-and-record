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

0 <= lists.length <= 10000
0 <= lists[i].length <= 500
-10000 <= lists[i][j] <= 10000
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10000.'''

#bf
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
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
#time complexity: O(nlogn) where n is the total number of nodes in all the linked lists.
#space complexity: O(n) where n is the total number of nodes in all the linked lists.

#iteration
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
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
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next
        return res.next
#time complexity: O(nk) where n is the total number of nodes in all the linked lists and k is the number of linked lists.
#space complexity: O(1) since we are not using any extra space except for the output linked list.