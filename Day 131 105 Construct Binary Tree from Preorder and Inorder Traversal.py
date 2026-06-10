'''You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000'''

#dfs
from typing import Optional, List
#definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: #base case, if preorder or inorder is empty, return None
            return None
        root = TreeNode(preorder[0]) #the first element in preorder is the root of the tree
        mid = inorder.index(preorder[0]) #find the index of the root in inorder
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid]) #build the left subtree using the left part of preorder and inorder
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) #build the right subtree using the right part of preorder and inorder
        return root
#time complexity: O(n^2) in worst case, O(n log n) in best case
#space complexity: O(n) in worst case, O(log n) in best case