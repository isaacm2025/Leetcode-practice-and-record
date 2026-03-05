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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#DFS
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
#time complexity: O(n^2) because of the index() function
#space complexity: O(n) because of the recursive stack and the new lists created by slicing

#Hashmap optimization
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_index = 0
        def dfs(left, right):
            if left > right:
                return None
            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            self.preorder_index += 1
            root.left = dfs(left, indices[root_val] - 1)
            root.right = dfs(indices[root_val] + 1, right)
            return root
        return dfs(0, len(inorder) - 1)
#time complexity: O(n) because we are visiting each node once and the index lookup is O(1)
#space complexity: O(n) because of the recursive stack and the hashmap storing the indices

#DFS optimal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder) or (limit is not None and inorder[inIdx] == limit):
                return None
            root_val = preorder[preIdx]
            root = TreeNode(root_val)
            preIdx += 1
            root.left = dfs(root_val)
            inIdx += 1
            root.right = dfs(limit)
            return root
        return dfs(None)
#time complexity: O(n) because we are visiting each node once
#space complexity: O(n) because of the recursive stack
