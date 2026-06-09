'''Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
'''

#dfs
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #if both p and q are None, we will return True indicating that the trees are equivalent.
            return True
        if p and q and p.val == q.val: #if both p and q are not None and the value of the current node in p is equal to the value of the current node in q, we will recursively call the isSameTree function on the left and right child of the current node in p and q to check if the left and right subtree are equivalent.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #if the left and right subtree are equivalent, we will return True indicating that the trees are equivalent. Otherwise, we will return False.
        else:
            return False #if one of p and q is None or the value of the current node in p is not equal to the value of the current node in q, we will return False indicating that the trees are not equivalent.
#time complexity: O(n) where n is the number of nodes in the trees. We visit each node once.
#space complexity: O(h) where h is the height of the trees. 
# In the best case, the trees are balanced and the height is log(n), so the space complexity is O(log(n)). 
# In the worst case, the space complexity is O(n) due to the recursive call stack.