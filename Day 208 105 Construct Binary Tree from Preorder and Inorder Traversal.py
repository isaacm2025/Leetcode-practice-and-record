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

1 <= inorder.length <= 2001.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
'''

#dfs
from typing import List, Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
#time complexity: O(n^2) because of the index() function
#space complexity: O(n) for the recursion stack and the tree itself

#hashmap + dfs
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0
        def dfs(l, r):
            if l > r:
                return None
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)
#time complexity: O(n) because we are using a hashmap to store the indices of the inorder array
#space complexity: O(n) for the recursion stack and the tree itself
