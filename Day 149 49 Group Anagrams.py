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

#sorting
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # create a defaultdict to store the anagrams, the default value is an empty list
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s) # append the original string to the list of anagrams for the sorted string
        return list(res.values()) # return the values of the dictionary as a list of lists
#time complexity: O(n * klogk) where n is the number of strings in strs and k is the maximum length of a string in strs, because we are sorting each string,
#space complexity: O(n * k) because we are storing the anagrams in a dictionary