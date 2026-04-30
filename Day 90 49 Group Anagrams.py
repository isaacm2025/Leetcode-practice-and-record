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

from collections import defaultdict
from typing import List
#sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
#time complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string in strs. This is because we sort each string which takes O(k log k) time and we do this for all n strings.
#space complexity: O(n * k) where n is the number of strings and k is the maximum length of a string in strs. This is because in the worst case, all strings could be anagrams of each other and we would store all n strings in the same list in the dictionary. 
# Additionally, we also store the sorted version of each string as a key in the dictionary, which also takes O(n * k) space in the worst case.