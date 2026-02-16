'''Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.'''

from typing import List
#sorting approach
from collections import defaultdict #import defaultdict for easier grouping

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Initialize a default dictionary to hold lists of anagrams
        for s in strs:
            sortedS = ''.join(sorted(s)) # Sort the string to create a key
            res[sortedS].append(s) # Append the original string to the list corresponding to the sorted key
        return list(res.values()) # Return the grouped anagrams as a list of lists
# Time Complexity: O(m * n log n) where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(m * n) where m is the number of unique anagram groups

#hash map counting approach
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Initialize a default dictionary to hold lists of anagrams
        for s in strs:
            count = [0] * 26 # Create a count array for 26 lowercase letters
            for c in s:
                count[ord(c) - ord('a')] += 1 # Count the frequency of each character in the string
            res[tuple(count)].append(s) # Use the count array as a key (converted to tuple) to group anagrams
        return list(res.values()) # Return the grouped anagrams as a list of lists
# Time Complexity: O(m * n) where n is the number of strings and k is the maximum length of a string
# Space Complexity: O(m) extra space for the hashmap
# space Complexity: O(m * n) space for the output list of lists
