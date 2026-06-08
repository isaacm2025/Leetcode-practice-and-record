'''Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true
Example 2:



Input: root = [1,2,3,null,null,4,null,5]

Output: false
Example 3:

Input: root = []

Output: true
Constraints:

The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000'''

#dfs
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): #we will use a helper function dfs to check if the tree is balanced and to calculate the height of the tree at the same time. 
            #The function will return a list of two elements: the first element is a boolean indicating whether the subtree rooted at the current node is balanced, 
            #and the second element is the height of the subtree rooted at the current node.
            if not node: #if the current node is None, we will return [True, 0] indicating that the subtree rooted at the current node is balanced and has a height of 0.
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right) #we will recursively call the dfs function on the left and right child of the current node to get the balance status and height of the left and right subtree.
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 #the subtree rooted at the current node is balanced if the left and right subtree are balanced and the difference in height between the left and right subtree is no more than 1.
            return [balanced, 1 + max(left[1], right[1])] #we will return a list of two elements: the first element is the balance status of the subtree rooted at the current node, and the second element is the height of the subtree rooted at the current node, which is 1 + max(left[1], right[1]) where left[1] and right[1] are the height of the left and right subtree respectively.
        return dfs(root)[0]
#time complexity: O(n) where n is the number of nodes in the tree. We visit each node once.
#space complexity: O(h) where h is the height of the tree. 
# In the best case, the tree is balanced and the height is log(n), so the space complexity is O(log(n)). 
# In the worst case, the space complexity is O(n) due to the recursive call stack.