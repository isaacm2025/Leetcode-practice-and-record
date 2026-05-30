'''You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"
Example 2:

Input: strs = ["dance","dag","danger","damage"]

Output: "da"
Example 3:

Input: strs = ["neet","feet"]

Output: ""
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] is made up of lowercase English letters if it is non-empty.
'''

#horitzontal scanning
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #initialize the prefix variable to the first string in the input list, which will be used to store the longest common prefix as we iterate through the list
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])): #iterate through the characters of the prefix and the current string in the input list, and compare them character by character until we find a mismatch or we reach the end of either string
                if prefix[j] != strs[i][j]: #if we find a mismatch, we break out of the loop and update the prefix variable to the substring of the prefix from the beginning to the index of the mismatch, which will be the longest common prefix of the strings we have compared so far
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
#time complexity: O(n*m) where n is the number of strings in the input list and m is the length of the longest common prefix
#space complexity: O(1) because we are using a constant amount of space to store the prefix variable and the loop variables

#vertical scanning
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
#time complexity: O(n*m) where n is the number of strings in the input list and m is the length of the longest common prefix
#space complexity: O(1) because we are using a constant amount of space to store the loop variables and the return value
                