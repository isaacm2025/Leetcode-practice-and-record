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
strs[i] is made up of lowercase English letters.
'''
from collections import defaultdict
from typing import List
#sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s)) #sort the characters in the string to get the key for the anagram group
            res[sorted_s].append(s) #append the original string to the list corresponding to the sorted key
        return list(res.values()) #return the list of anagram groups
#time complexity: O(n k log k) where n is the number of strings and k is the maximum length of a string in strs (due to sorting each string)
#space complexity: O(n k) in the worst case when all strings are anagrams of each other, resulting in a single group containing all strings
