'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3], k = 1

Output: 1
Example 2:



Input: root = [4,3,5,2,null], k = 4

Output: 5
Constraints:

1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000'''

# Definition for a binary tree node.
from typing import Optional
#bf
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        arr.sort()
        return arr[k - 1]
#time complexity: O(nlogn) where n is the number of nodes in the tree
#space complexity: O(n) where n is the number of nodes in the tree

#inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k - 1]
#time complexity: O(n) where n is the number of nodes in the tree
#space complexity: O(n) where n is the number of nodes in the tree

#iterative DFS
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
#time complexity: O(n) where n is the number of nodes in the tree
#space complexity: O(n) where n is the number of nodes in the tree
