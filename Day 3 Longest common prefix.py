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

#Horizontal scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # Initialize prefix as the first string
        for i in range(1, len(strs)): # Iterate through the rest of the strings
            j = 0 # Initialize index for comparison
            while j < min(len(prefix), len(strs[i])): # Compare characters until the end of the shorter string
                if prefix[j] != strs[i][j]: # If characters don't match,
                    break
                j += 1 # Move to the next character
            prefix = prefix[:j] # Update prefix to the common part
        return prefix # Return the longest common prefix
# Time Complexity: O(n*m) where n is the number of strings and m is the length of the shortest string
# Space Complexity: O(1)

#Vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # Iterate through characters of the first string
            for s in strs: # Compare with each string in the array
                if i == len(s) or s[i] != strs[0][i]: # If index exceeds length or characters don't match
                    return s[:i] # Return the common prefix up to the mismatch
        return strs[0] # If no mismatch found, return the entire first string
# Time Complexity: O(n*m) where n is the number of strings and m is the length of the shortest string
# Space Complexity: O(1)

#sorting approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort() # Sort the array of strings
        for i in range(min(len(strs[0]), len(strs[-1]))): # Compare characters of the first and last strings
            if strs[0][i] != strs[-1][i]: # If characters don't match
                return strs[0][:i] # Return the common prefix up to the mismatch
        return strs[0] # If no mismatch found, return the entire first string
# Time Complexity: O(n*m log m) due to sorting
# Space Complexity: O(1) or O(m) depending on the sorting algorithm used


