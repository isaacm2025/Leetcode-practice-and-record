'''Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:



Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:



Input: head = [1,2], index = -1

Output: false
Constraints:

0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.'''

#hashset
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set() #create a set to keep track of the nodes we have already visited. This allows us to efficiently check for cycles in the linked list.
        cur = head #initialize a pointer cur to traverse the linked list starting from the head node.
        while cur:
            if cur in seen:
                return True
            seen.add(cur) #add the current node to the set of visited nodes.
            cur = cur.next
        return False 
#time complexity: O(n)
#space complexity: O(n)



#two pointer
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next: #the loop continues as long as fast and fast.next are not None. This ensures that we don't encounter a NoneType error when trying to access fast.next.next.
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #if the slow and fast pointers meet, it indicates that there is a cycle in the linked list. This is because the fast pointer moves at twice the speed of the slow pointer, so if there is a cycle, they will eventually meet at some point within the cycle.
                return True
        return False
#time complexity: O(n)
#space complexity: O(1)