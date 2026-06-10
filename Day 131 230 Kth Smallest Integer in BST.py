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

#defition for a binary tree node.
#bf
from typing import Optional
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
        return arr[k-1]
#time complexity: O(n log n)
#space complexity: O(n)

#inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(node):
            if not node: #base case, if node is None, return
                return
            dfs(node.left) #traverse left subtree
            arr.append(node.val) #append current node value to arr
            dfs(node.right) #traverse right subtree
        dfs(root) #start dfs traversal from root
        return arr[k-1] #return the k-1 th element in arr, which is the kth smallest element in the tree
#time complexity: O(n)
#space complexity: O(n) in worst case, O(log n) in best case


#recursive dfs
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val
        def dfs(node):
            nonlocal count, res
            if not node:
                return
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
#time complexity: O(h + k) where h is the height of the tree
#space complexity: O(h) where h is the height of the tree, worst case O(n) when the tree is skewed, best case O(log n) when the tree is balanced