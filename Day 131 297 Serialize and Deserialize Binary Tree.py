'''Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:



Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
'''

#dfs
from typing import Optional
#definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N") #append "N" to res if node is None
                return
            res.append(str(node.val)) #append the value of the current node to res
            dfs(node.left) #traverse left subtree
            dfs(node.right)
        dfs(root) #start dfs traversal from root
        return ",".join(res) #join the elements in res with "," and return the resulting
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") #split the input string by "," to get a list of values
        self.index = 0 #initialize index to 0
        def dfs():
            if vals[self.index] == "N":
                self.index += 1 #increment index, because we have used the current value
                return None
            node = TreeNode(int(vals[self.index])) #create a new TreeNode with the current
            self.index += 1 #increment index, because we have used the current value
            node.left = dfs() #build the left subtree
            node.right = dfs() #build the right subtree
            return node
        return dfs() #start dfs traversal to build the tree from the list of values
#time complexity: O(n)
#space complexity: O(n)