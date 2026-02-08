'''You are given an array of characters which represents a string s. Write a function which reverses a string.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["n","e","e","t"]

Output: ["t","e","e","n"]
Example 2:

Input: s = ["r","a","c","e","c","a","r"]

Output: ["r","a","c","e","c","a","r"]
Constraints:

1 <= s.length < 100,000
s[i] is a printable ascii character.'''

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    tmp = []
    for i in range(len(s) -1, -1, -1):
        tmp.append(s[i])
    for i in range(len(s)):
        s[i] = tmp[i]
#time complexity: O(n)
#space complexity: O(n)

#build-in function
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
#time coomplexity: O(n)
#space complexity: O(1)
